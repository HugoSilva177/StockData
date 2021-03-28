from web_scraping.fundamentus.src.dao.mongo_db.AbstractMongoDAO import AbstractMongoDAO
from web_scraping.fundamentus.src.connect_db.DAConexaoMongo import DAConexaoMongo


class InfoEmpresaDAO(AbstractMongoDAO):

    def __init__(self, banco_dados="mongodb", nome_colecao="info_empresa"):
        super().__init__()
        self.__erro = None
        self.__colecao_mongo = None
        try:
            self.__colecao_mongo = DAConexaoMongo(banco_dados, nome_colecao).get_colecao_mongo()
        except Exception:
            self.__erro = "Falha em estabelecer conexao com a coleção 'dados_empresa' no MongoDB"

    def buscar_dados_empresa(self, papel, data=None):
        dados_empresa = self.__colecao_mongo.find_one({"Papel": papel})
        return dados_empresa

    def get_erro(self):
        return self.__erro