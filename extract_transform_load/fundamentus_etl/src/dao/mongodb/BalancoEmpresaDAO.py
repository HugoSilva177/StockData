from extract_transform_load.fundamentus_etl.src.connect_db.DAConexaoMongo import DAConexaoMongo
from extract_transform_load.fundamentus_etl.src.dao.mongodb.AbstractMongoDAO import AbstractMongoDAO


class BalancoEmpresaDAO(AbstractMongoDAO):

    def __init__(self, banco_dados="mongodb_docker", nome_colecao="balanco_empresa"):
        super().__init__()
        self.__erro = None
        self.__colecao_mongo = None
        try:
            self.__colecao_mongo = DAConexaoMongo(banco_dados, nome_colecao).get_colecao_mongo()
        except Exception:
            self.__erro = "Falha em estabelecer conexao com a coleção 'balanco_empresa' no MongoDB"

    def inserir_dados(self, balanco_empresa):
        print('** Incluindo dados do balanço...')
        id_balanco_inserido = self.__colecao_mongo.insert_one(balanco_empresa).inserted_id
        return id_balanco_inserido