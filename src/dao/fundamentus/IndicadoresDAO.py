from src.connect_db.DAConexaoMongo import DAConexaoMongo
from src.dao.fundamentus.AbstractMongoDAO import AbstractMongoDAO
from src.dao.fundamentus.CotacaoEmpresaDAO import CotacaoEmpresaDAO


class IndicadoresDAO(AbstractMongoDAO):

        def __init__(self, id_inserido_cotacao, banco_dados="fundamentus", nome_colecao="indicadores_empresa"):
            super().__init__()
            self.__erro = None
            self.__colecao_mongo = None
            self.__cotacao_dao = CotacaoEmpresaDAO()
            self.__id_inserido_cotacao = id_inserido_cotacao
            try:
                self.__colecao_mongo = DAConexaoMongo(banco_dados, nome_colecao).get_colecao_mongo( )
            except Exception:
                self.__erro = "Falha em estabelecer conexao com a coleção 'indicadores_empresa' no MongoDB"

        def inserir_dados(self, indicadores_fundamentalistas_empresa):
            id_inserido_indicadores = self.__colecao_mongo.insert_one(indicadores_fundamentalistas_empresa).inserted_id
            self.get_conexao_cotacao().inserir_indicadores_na_cotacao(self.__id_inserido_cotacao,
                                                                      id_inserido_indicadores)

        def get_conexao_cotacao(self):
            return self.__cotacao_dao

        def get_erro(self):
            return self.__erro