from extract_transform_load.fundamentus_etl.etl_mongodb.src.dao.AbstractMongoDAO import AbstractMongoDAO
from extract_transform_load.fundamentus_etl.etl_mongodb.src.connect_db.DAConexaoMongo import DAConexaoMongo


class CotacaoEmpresaDAO(AbstractMongoDAO):

    def __init__(self, nome_banco="fundamentus", nome_colecao="cotacao_empresa"):
        super().__init__()
        self.__erro = None
        self.__colecao_mongo = None
        try:
            self.__colecao_mongo = DAConexaoMongo(nome_banco, nome_colecao).get_colecao_mongo()
        except Exception:
            self.__erro = "Falha em estabelecer conexao com a coleção 'cotacao_empresa' no MongoDB"


    def inserir_dados(self, cotacao_empresa):
        id_inserido_cotacao = self.__colecao_mongo.insert_one(cotacao_empresa).inserted_id
        return id_inserido_cotacao

    def inserir_oscilacoes_na_cotacao(self, id_inserido_cotacao, id_inserido_oscilacao):
        self.__colecao_mongo.update_one({"_id": id_inserido_cotacao},
                                        {"$set": {"Oscilacao": id_inserido_oscilacao}})

    def inserir_indicadores_na_cotacao(self, id_inserido_cotacao, id_inserido_indicadores):
        self.__colecao_mongo.update_one({"_id": id_inserido_cotacao},
                                        {"$set": {"Indicador_Fundamentalista": id_inserido_indicadores}})

    def get_erro(self):
        return self.__erro