from extract_transform_load.fundamentus_etl.src.dao.mongodb.AbstractMongoDAO import AbstractMongoDAO
from extract_transform_load.fundamentus_etl.src.connect_db.DAConexaoMongo import DAConexaoMongo


class InfoEmpresaDAO(AbstractMongoDAO):

    def __init__(self, banco_dados="mongodb_docker", nome_colecao="info_empresa"):
        super().__init__()
        self.__erro = None
        self.__colecao_mongo = None
        try:
            self.__colecao_mongo = DAConexaoMongo(banco_dados, nome_colecao).get_colecao_mongo()
        except Exception:
            self.__erro = "Falha em estabelecer conexao com a coleção 'dados_empresa' no MongoDB"

    def inserir_dados(self, info_empresa):
        print('-------------------------------------')
        print('Dados da empresa não existe!')
        print('* Incluindo dados da empresa...')
        id_empresa_inserida = self.__colecao_mongo.insert_one(info_empresa).inserted_id
        return id_empresa_inserida

    def get_erro(self):
        return self.__erro