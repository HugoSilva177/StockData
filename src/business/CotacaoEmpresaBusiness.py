from src.etl.CotacaoEmpresaETL import CotacaoEmpresaETL
from src.etl.OscilacoesEmpresaETL import OscilacoesEmpresaETL
from src.etl.IndicadoresEmpresaETL import IndicadoresEmpresaETL


class CotacaoEmpresaBusiness:

    def __init__(self, papel, id_empresa_inserida):
        self.__papel = papel
        self.__id_inserido_cotacao = None
        self.__id_empresa_inserida = id_empresa_inserida


    def iniciar_web_scraping(self):
        self.__cotacao_web_scraping()
        self.__oscilacoes_web_scraping()
        self.__indicadores_web_scraping()


    def __cotacao_web_scraping(self):
        cotacao_etl = CotacaoEmpresaETL(self.__papel, self.__id_empresa_inserida)
        self.__id_inserido_cotacao = cotacao_etl.iniciar_cotacao_etl()

    def __oscilacoes_web_scraping(self):
        oscilacoes_etl = OscilacoesEmpresaETL(self.__papel, self.__id_inserido_cotacao)
        oscilacoes_etl.iniciar_oscilacoes_etl()

    def __indicadores_web_scraping(self):
        indicadores_etl = IndicadoresEmpresaETL(self.__papel, self.__id_inserido_cotacao)
        indicadores_etl.iniciar_indicadores_etl()







