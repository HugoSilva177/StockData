from src.dao.fundamentus.AbstractMongoDAO import AbstractMongoDAO
from src.connect_db.DAConexaoMongo import DAConexaoMongo


class CotacaoEmpresaDAO(AbstractMongoDAO):

    def __init__(self):
        super().__init__()
        self.__erro = None
        self.__colecao_mongo = None
        try:
            self.__colecao_mongo = DAConexaoMongo('fundamentus', 'cotacao_empresa').get_colecao_mongo()
        except Exception:
            self.__erro = "Falha em estabelecer conexao com a coleção 'cotacao_empresa' no MongoDB"


    def inserir_dados(self, cotacao_empresa):
        print('** Incluindo dados da cotação...')
        id_inserido_cotacao = self.__colecao_mongo.insert_one(cotacao_empresa).inserted_id
        return id_inserido_cotacao

    def inserir_oscilacoes_na_cotacao(self, id_inserido_cotacao, id_inserido_oscilacao):
        self.__colecao_mongo.update_one({"_id": id_inserido_cotacao},
                                        {"$set": {"Oscilacao": id_inserido_oscilacao}})

    def inserir_indicadores_na_cotacao(self, id_inserido_cotacao, id_inserido_indicadores):
        self.__colecao_mongo.update_one({"_id": id_inserido_cotacao},
                                        {"$set": {"Indicador_Fundamentalista": id_inserido_indicadores}})

    def buscar_lista_cotacoes_empresa_por_papel(self, papel):
        lista_cotacoes = self.__colecao_mongo.find({"Papel": papel})
        return lista_cotacoes

    def buscar_cotacao_empresa_por_papel_data(self, papel, data_cotacao):
        cotacao_por_papel_data = self.__colecao_mongo.find_one({"Papel": papel,
                                                                "Data_ult_cot": data_cotacao})
        return cotacao_por_papel_data

    def buscar_cotacao_empresa_por_id_empresa_data(self, id_empresa, data_cotacao):
        cotacao_por_id_data = self.__colecao_mongo.find_one({"Empresa": id_empresa,
                                                             "Data_ult_cot": data_cotacao})
        return cotacao_por_id_data

    def get_erro(self):
        return self.__erro