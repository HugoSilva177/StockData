from web_scraping.fundamentus.src.connect_db.DAConexaoFactory import DAConexaoFactory


class DAConexaoMongo(DAConexaoFactory):

    def __init__(self, nome_banco, nome_colecao):
        super().__init__()
        self.__nome_banco = nome_banco
        self.__nome_colecao = nome_colecao
        self.__colecao_mongo = None
        self.__erro = None
        try:
            conexao_mongo = self._get_conexao('mongodb_docker', self.__nome_banco)
            self.__colecao_mongo = conexao_mongo[self.__nome_colecao]
        except Exception:
            self.__erro = 'Erro ao criar conexão com MongoDB'

    def get_colecao_mongo(self):
        return self.__colecao_mongo

    def get_erro(self):
        return self.__erro