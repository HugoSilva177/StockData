from src.connect_db.DAConexaoMongo import DAConexaoMongo
from src.dao.fundamentus.AbstractMongoDAO import AbstractMongoDAO


class OscilacoesEmpresaDAO(AbstractMongoDAO):

    def __init__(self, banco_dados="fundamentus", nome_colecao="oscilacoes_empresa"):
        super().__init__()
        self.__erro = None
        self.__colecao_mongo = None
        try:
            self.__colecao_mongo = DAConexaoMongo(banco_dados, nome_colecao).get_colecao_mongo()
        except Exception:
            self.__erro = "Falha em estabelecer conexao com a coleção 'oscilacoes_empresa' no MongoDB"

    def inserir_dados(self, oscilacoes_empresa):
        id_inserido_oscilacao = self.__colecao_mongo.insert_one(oscilacoes_empresa).inserted_id
        return id_inserido_oscilacao

    def get_erro(self):
        return self.__erro