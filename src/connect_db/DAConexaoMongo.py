from src.connect_db.DAConexaoFactory import DAConexaoFactory


class DAConexaoMongo(DAConexaoFactory):

    def __init__(self, nome_banco, colecao_nome):
        super().__init__()
        self.__nome_banco = nome_banco
        self.__colecao_nome = colecao_nome
        self.__colecao_mongo = None
        self.__erro = None
        try:
            conexao_mongo = self.get_conexao('mongodb', self.__nome_banco)
            self.__colecao_mongo = conexao_mongo[self.__colecao_nome]
        except Exception:
            self.__erro = 'Erro ao criar conexão com MongoDB'


    def get_colecao_mongo(self):
        return self.__colecao_mongo

    def get_erro(self):
        return self.__erro