from src.connect_db.DAConexaoMongo import DAConexaoMongo


class CotacaoEmpresaDAO:

    def __init__(self):
        self.__erro = None
        self.__colecao_mongo = None
        self.__id_inserido_cotacao = None
        try:
            self.__colecao_mongo = DAConexaoMongo('fundamentus', 'cotacao_empresa').get_colecao_mongo()
        except Exception:
            self.__erro = "Falha em estabelecer conexao com a coleção 'cotacao_empresa' no MongoDB"


    def buscar_lista_cotacoes_empresa_por_papel(self, papel):
        lista_cotacoes = self.__colecao_mongo.find({"Papel": papel})
        return lista_cotacoes

    def buscar_cotacao_empresa_por_papel_data(self, papel, data_cotacao):
        cotacao_por_papel = self.__colecao_mongo.find_one({"Papel": papel,
                                                           "Data_ult_cot": data_cotacao})
        return cotacao_por_papel

    def inserir_cotacao_empresa(self, cotacao_empresa):
        self.__id_inserido_cotacao = self.__colecao_mongo.insert_one(cotacao_empresa).inserted_id

    def atualizar_oscilacao_na_cotacao(self, id_inserido_oscilacoes, id_inserido_cotacao):
        self.__colecao_mongo.update_one({"_id": id_inserido_cotacao},
                                        {"$set": {"Oscilacao": id_inserido_oscilacoes}})

    def atualizar_indicadores_fundamentalistas_na_cotacao(self, id_inserido_indicadores, id_inserido_cotacao):
        self.__colecao_mongo.update_one({"_id": id_inserido_cotacao},
                                        {"$set": {"Indicador_Fundamentalista": id_inserido_indicadores}})

    def get_id_inserido_cotacao(self):
        return self.__id_inserido_cotacao

    def get_erro(self):
        return self.__erro