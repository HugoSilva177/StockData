from src.etl.CotacaoEmpresaETL import CotacaoEmpresaETL
from src.etl.OscilacoesEmpresaETL import OscilacoesEmpresaETL


class CotacaoEmpresaBusiness:

    def __init__(self, papel):
        self.__papel = papel
        self.__cotacao_etl = CotacaoEmpresaETL(papel)
        self.__oscilacoes_etl = OscilacoesEmpresaETL(papel)

    def iniciar_cotacao_scraping_etl(self):
        cotacao_empresa_label, cotacao_empresa_dados = self.__cotacao_etl.extrair_dados_cotacao_empresa()
        cotacao_empresa = self.__cotacao_etl.transformar_dados_cotacao_empresa(cotacao_empresa_label, cotacao_empresa_dados)
        self.__cotacao_etl.adicionar_dados_cotacao_empresa_db(cotacao_empresa)


    def iniciar_oscilacoes_scraping_etl(self):
        oscilacoes_empresa_label, oscilacoes_empresa_dados = self.__oscilacoes_etl.extrair_dados_oscilacoes_empresa( )
        oscilacoes_empresa = self.__oscilacoes_etl.transformar_dados_oscilacoes_empresa(oscilacoes_empresa_label,
                                                                         oscilacoes_empresa_dados)
        self.__oscilacoes_etl.adicionar_dados_cotacao_empresa_db(oscilacoes_empresa)




