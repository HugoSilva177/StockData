from web_scraping.fundamentus.src.dao.mongo_db.AbstractMongoDAO import AbstractMongoDAO
from web_scraping.fundamentus.src.connect_db.DAConexaoMongo import DAConexaoMongo


class CotacaoEmpresaDAO(AbstractMongoDAO):

    def __init__(self, banco_dados="mongodb_docker", nome_colecao="cotacao_empresa"):
        super().__init__()
        self.__erro = None
        self.__colecao_mongo = None
        try:
            self.__colecao_mongo = DAConexaoMongo(banco_dados, nome_colecao).get_colecao_mongo()
        except Exception:
            self.__erro = "Falha em estabelecer conexao com a coleção 'cotacao_empresa' no MongoDB"


    def buscar_dados_empresa(self, papel, data_cotacao=None):
        cotacao_por_papel_data = self.__colecao_mongo.find_one({"Papel": papel,
                                                                "Data_ult_cot": data_cotacao})
        return cotacao_por_papel_data

    def get_erro(self):
        return self.__erro