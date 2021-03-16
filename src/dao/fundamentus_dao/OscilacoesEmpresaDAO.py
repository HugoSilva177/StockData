from src.connect_db.DAConexaoMongo import DAConexaoMongo
from src.dao.fundamentus_dao.CotacaoEmpresaDAO import CotacaoEmpresaDAO


class OscilacoesEmpresaDAO:

    def __init__(self):
        self.__erro = None
        self.__colecao_mongo = None
        self.__cotadao_dao = CotacaoEmpresaDAO()
        try:
            self.__colecao_mongo = DAConexaoMongo('fundamentus', 'oscilacoes_empresa').get_colecao_mongo()
        except Exception:
            self.__erro = "Falha em estabelecer conexao com a coleção 'oscilacoes_empresa' no MongoDB"

    def inserir_oscilacoes_empresa_mongodb(self, oscilacoes_empresa, id_inserido_cotacao):
        oscilacoes_empresa['Cotacao'] = id_inserido_cotacao
        id_inserido_oscilacao = self.__colecao_mongo.insert_one(oscilacoes_empresa).inserted_id
        self.get_conexao_cotacao().inserir_oscilacoes_na_cotacao(id_inserido_cotacao, id_inserido_oscilacao)

    def get_conexao_cotacao(self):
        return self.__cotadao_dao

    def get_erro(self):
        return self.__erro