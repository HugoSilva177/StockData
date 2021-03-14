from src.conexao_db.DAConexaoFactory import DAConexaoFactory

class CotacaoEmpresaDAO():

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



    def buscar_lista_cotacoes_empresa_por_papel(self, papel):
        pass

    def buscar_cotacao_empresa_por_papel_data(self, papel, data_cotacao):
        pass

    def inserir_cotacao_empresa(self, cotacao_empresa):
        pass

    def atualizar_oscilacao_na_cotacao(self, id_inserido_oscilacoes, id_inserido_cotacao):
        pass

    def atualizar_indicadores_fundamentalistas_na_cotacao(self, id_inserido_indicadores, id_inserido_cotacao):
        pass
