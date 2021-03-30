from web_scraping.fundamentus.src.scraping.InfoEmpresaScraping import InfoEmpresaScraping
from web_scraping.fundamentus.src.scraping.BalancoEmpresaScraping import BalancoEmpresaScraping
from web_scraping.fundamentus.src.scraping.CotacaoEmpresaScraping import CotacaoEmpresaScraping
from web_scraping.fundamentus.src.business.empresa_business.EmpresaBusiness import EmpresaBusiness
from web_scraping.fundamentus.src.scraping.OscilacoesEmpresaScraping import OscilacoesEmpresaScraping
from web_scraping.fundamentus.src.scraping.IndicadoresEmpresaScraping import IndicadoresEmpresaScraping


class WebScrapingBusiness:

    def __init__(self, papel):
        self.__papel = papel
        self.__dados_empresa_label_valores = {}

    def dados_empresa_web_scraping(self):
        self.info_empresa_web_scraping()
        self.cotacao_empresa_web_scraping()
        self.balanco_empresa_web_scraping()
        return self.__dados_empresa_label_valores

    def info_empresa_web_scraping(self):
        print('** Web Scraping dados empresa...')
        info_empresa_scraping = EmpresaBusiness(InfoEmpresaScraping(self.__papel))
        self.__dados_empresa_label_valores['Info'] = info_empresa_scraping.iniciar_web_scraping()

    def cotacao_empresa_web_scraping(self):
        print('** Web Scraping dados cotação...')
        cotacao_scraping = EmpresaBusiness(CotacaoEmpresaScraping(self.__papel))
        oscilacoes_scraping = EmpresaBusiness(OscilacoesEmpresaScraping(self.__papel))
        indicadores_scraping = EmpresaBusiness(IndicadoresEmpresaScraping(self.__papel))
        self.__dados_empresa_label_valores['Cotacao'] = cotacao_scraping.iniciar_web_scraping()
        self.__dados_empresa_label_valores['Oscilacoes'] = oscilacoes_scraping.iniciar_web_scraping()
        self.__dados_empresa_label_valores['Indicadores'] = indicadores_scraping.iniciar_web_scraping()

    def balanco_empresa_web_scraping(self):
        print('** Web Scraping dados balanço...')
        balanco_scraping = EmpresaBusiness(BalancoEmpresaScraping(self.__papel))
        self.__dados_empresa_label_valores['Balanco'] = balanco_scraping.iniciar_web_scraping()

    def get_dados_empresa_label_valores(self):
        return self.__dados_empresa_label_valores
