from src.connect_db.DAConexaoMongo import DAConexaoMongo
from abc import ABCMeta, abstractmethod


class AbstractMongoDAO(metaclass=ABCMeta):

    @abstractmethod
    def inserir_dados(self, dados_empresa):
        return
