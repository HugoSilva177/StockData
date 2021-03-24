from src.dao.mongodb.AbstractMongoDAO import AbstractMongoDAO
from src.connect_db.DAConexaoMongo import DAConexaoMongo


class InfoEmpresaDAO(AbstractMongoDAO):

    def __init__(self, banco_dados="mongodb", nome_colecao="info_empresa"):
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

    def buscar_dados_empresa_por_papel(self, papel):
        dados_empresa = self.__colecao_mongo.find_one({"Papel": papel})
        return dados_empresa

    def buscar_dados_empresa_por_id(self, id_empresa):
        dados_empresa = self.__colecao_mongo.find_one({"_id": id_empresa})
        return dados_empresa

    def get_erro(self):
        return self.__erro