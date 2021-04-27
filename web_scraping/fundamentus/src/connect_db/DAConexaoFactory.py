from pymongo import MongoClient


class DAConexaoFactory:

    def __init__(self):
        self.__erro_conexao = None
        self.__factory = None
        self.__mongo_db = 'mongodb_docker'
        self.__hdfs = 'hdfs'

    def _get_conexao(self, banco_tipo, nome_banco):
        conexao_db = None
        self.__factory = banco_tipo
        if banco_tipo == self.__mongo_db:
            url_conexao = 'mongodb://localhost:27017/'
            try:
                cliente_db = MongoClient(url_conexao)
                conexao_db = cliente_db[nome_banco]
            except Exception:
                self.__erro_conexao = 'Erro ao conectar no MongoDB (mongodb_docker)'
        elif banco_tipo == self.__hdfs:
            url_conexao = 'hdfs://172.17.177.40:9000/user/hadoopuser/'
            try:
                conexao_db = url_conexao + nome_banco
            except Exception:
                self.__erro_conexao = 'Erro ao conectar no Cluster Hadoop'
        return conexao_db

    def get_erros(self):
        return self.__erro_conexao

    def get_factory(self):
        return self.__factory
