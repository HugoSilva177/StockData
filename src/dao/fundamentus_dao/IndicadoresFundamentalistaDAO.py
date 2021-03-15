from src.connect_db.DAConexaoFactory import DAConexaoFactory

class IndicadoresFundamentalistaDAO():

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



    def inserir_indicadores_fundamentalista_empresa_mongodb(self, indicadores_fundamentalitas_empresa, id_inserido_cotacao):
        pass