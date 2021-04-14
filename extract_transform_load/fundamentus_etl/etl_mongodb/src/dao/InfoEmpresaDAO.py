from extract_transform_load.fundamentus_etl.etl_mongodb.src.dao.AbstractMongoDAO import AbstractMongoDAO
from extract_transform_load.fundamentus_etl.etl_mongodb.src.connect_db.DAConexaoMongo import DAConexaoMongo


class InfoEmpresaDAO(AbstractMongoDAO):

    def __init__(self, nome_banco="fundamentus", nome_colecao="info_empresa"):
        super().__init__()
        self.__erro = None
        self.__colecao_mongo = None
        try:
            self.__colecao_mongo = DAConexaoMongo(nome_banco, nome_colecao).get_colecao_mongo()
        except Exception:
            self.__erro = "Falha em estabelecer conexao com a coleção 'dados_empresa' no MongoDB"

    def inserir_dados(self, info_empresa):
        id_empresa_inserida = self.__colecao_mongo.insert_one(info_empresa).inserted_id
        return id_empresa_inserida

    def get_erro(self):
        return self.__erro