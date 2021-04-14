from web_scraping.fundamentus.src.connect_db.DAConexaoMongo import DAConexaoMongo
from web_scraping.fundamentus.src.dao.mongo_db.AbstractMongoDAO import AbstractMongoDAO

class BalancoEmpresaDAO(AbstractMongoDAO):

    def __init__(self, nome_banco="fundamentus", nome_colecao="balanco_empresa"):
        super().__init__()
        self.__erro = None
        self.__colecao_mongo = None
        try:
            self.__colecao_mongo = DAConexaoMongo(nome_banco, nome_colecao).get_colecao_mongo()
        except Exception:
            self.__erro = "Falha em estabelecer conexao com a coleção 'balanco_empresa' no MongoDB"


    def buscar_dados_empresa(self, papel, data_balanco=None):
        balanco_papel_data = self.__colecao_mongo.find_one({"Papel": papel,
                                                            "Ult_balanco_processado": data_balanco})
        return balanco_papel_data