from src.conexao_db.DAConexaoFactory import DAConexaoFactory

class InfoEmpresaDAO():

    def __init__(self):
        self.__erro = None
        self.__con = None
        self.__factory = None

        try:
            conexao = DAConexaoFactory()
            self.__con = conexao.getConexao('mongodb', 'fundamentus')
            self.__factory = conexao.getFactory()
        except Exception:
            self.__erro = 'Falha em estabelecer conexao com MongoDB'

    def buscar_dados_empresa_por_papel(self, papel):
        pass


    def inserir_dados_empresa(self, info_empresa):
        pass