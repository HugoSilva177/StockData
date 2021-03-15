from pymongo import MongoClient


class DAConexaoFactory:

    def __init__(self):
        self.__erroConexao = None
        self.__factory = None
        self.__mongo_db = 'mongodb'
        self.__hadoop_hdfs = 'hadoop'
        self.__mysql = 'mysql'

    def get_conexao(self, banco_tipo, banco_nome):
        conexao_db = None
        self.__factory = banco_tipo
        if(banco_tipo == self.__mongo_db):
            url_conexao = 'mongodb://localhost:27017/'
            try:
                cliente_db = MongoClient(url_conexao)
                conexao_db = cliente_db[banco_nome]
            except Exception:
                self.__erroConexao = 'Erro ao conectar no MongoDB (fundamentus)'
        if(banco_tipo == self.__hadoop_hdfs):
            pass
        return conexao_db

    def getErros(self):
        return self.__erroConexao

    def getFactory(self):
        return self.__factory