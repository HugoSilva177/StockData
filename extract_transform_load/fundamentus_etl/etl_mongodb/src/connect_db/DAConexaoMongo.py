from pymongo import MongoClient


class DAConexaoMongo:

    def __init__(self, nome_banco, colecao_nome):
        self.__nome_banco = nome_banco
        self.__colecao_nome = colecao_nome
        self.__erro_conexao = None

    def get_colecao_mongo(self):
        conexao_mongo = self.__get_conexao()
        colecao_mongo = conexao_mongo[self.__colecao_nome]
        return colecao_mongo

    def __get_conexao(self):
        url_conexao = 'mongodb_docker://localhost:27017/'
        try:
            cliente_db = MongoClient(url_conexao)
            conexao_db = cliente_db[self.__nome_banco]
            return conexao_db
        except Exception:
            self.__erro_conexao = 'Erro ao conectar no MongoDB (mongodb_docker)'

    def get_erro(self):
        return self.__erro_conexao