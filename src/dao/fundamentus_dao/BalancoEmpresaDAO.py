from src.conexao_db.DAConexaoFactory import DAConexaoFactory

class BalancoEmpresaDAO():

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

    def buscar_balanco_empresa_por_papel(self, papel):
        pass

    def buscar_lista_balancos_empresa_por_papel_data(self, papel, data_balanco):
        pass

    def inserir_balanco_empresa(self, info_empresa):
        pass

    def atualizar_cotacoes_no_balanco_por_id(self, id_inserido_balanco, id_inserido_cotacao):
        pass

    def atualizar_cotacoes_no_balanco_por_papel_data(self, papel, data_ult_balanco, id_inserido_cotacao):
        pass