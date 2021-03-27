from abc import ABCMeta, abstractmethod


class AbstractMongoDAO(metaclass=ABCMeta):

    @abstractmethod
    def buscar_dados_empresa(self, papel, data_cotacao=None):
        return


