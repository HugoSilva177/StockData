from src.connect_db.DAConexaoMongo import DAConexaoMongo
from src.dao.fundamentus_dao.CotacaoEmpresaDAO import CotacaoEmpresaDAO

class IndicadoresFundamentalistaDAO():

        def __init__(self):
            self.__erro = None
            self.__colecao_mongo = None
            self.__cotadao_dao = CotacaoEmpresaDAO()
            try:
                self.__colecao_mongo = DAConexaoMongo('fundamentus', 'indicadores_empresa').get_colecao_mongo( )
            except Exception:
                self.__erro = "Falha em estabelecer conexao com a coleção 'indicadores_empresa' no MongoDB"

        def inserir_indicadores_empresa_mongodb(self, indicadores_fundamentalistas_empresa, id_inserido_cotacao):
            indicadores_fundamentalistas_empresa['Cotacao'] = id_inserido_cotacao
            id_inserido_indicadores = self.__colecao_mongo.insert_one(indicadores_fundamentalistas_empresa).inserted_id
            self.get_conexao_cotacao().inserir_indicadores_fundamentalistas_na_cotacao(id_inserido_cotacao, id_inserido_indicadores)

        def get_conexao_cotacao(self):
            return self.__cotadao_dao

        def get_erro(self):
            return self.__erro