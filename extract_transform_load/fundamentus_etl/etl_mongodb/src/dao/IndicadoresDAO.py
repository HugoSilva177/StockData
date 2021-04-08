from extract_transform_load.fundamentus_etl.etl_mongodb.src.connect_db.DAConexaoMongo import DAConexaoMongo
from extract_transform_load.fundamentus_etl.etl_mongodb.src.dao.AbstractMongoDAO import AbstractMongoDAO


class IndicadoresDAO(AbstractMongoDAO):

        def __init__(self, banco_dados="fundamentus", nome_colecao="indicadores_empresa"):
            super().__init__()
            self.__erro = None
            self.__colecao_mongo = None
            try:
                self.__colecao_mongo = DAConexaoMongo(banco_dados, nome_colecao).get_colecao_mongo( )
            except Exception:
                self.__erro = "Falha em estabelecer conexao com a coleção 'indicadores_empresa' no MongoDB"

        def inserir_dados(self, indicadores_fundamentalistas_empresa):
            id_inserido_indicadores = self.__colecao_mongo.insert_one(indicadores_fundamentalistas_empresa).inserted_id
            return id_inserido_indicadores

        def get_erro(self):
            return self.__erro