from web_scraping.fundamentus.src.business.empresa_business.InfoEmpresaBusiness import InfoEmpresaBusiness
from web_scraping.fundamentus.src.business.empresa_business.BalancoEmpresaBusiness import BalancoEmpresaBusiness
from web_scraping.fundamentus.src.business.empresa_business.CotacaoEmpresaBusiness import CotacaoEmpresaBusiness
from web_scraping.fundamentus.src.business.empresa_business.OscilacoesEmpresaBusiness import OscilacoesEmpresaBusiness
from web_scraping.fundamentus.src.business.empresa_business.IndicadoresEmpresaBusiness import IndicadoresEmpresaBusiness


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
        self.__dados_empresa_label_valores['Info'] = InfoEmpresaBusiness(self.__papel).iniciar_web_scraping()
        return self.__dados_empresa_label_valores

    def cotacao_empresa_web_scraping(self):
        self.__dados_empresa_label_valores['Cotacao'] = CotacaoEmpresaBusiness(self.__papel).iniciar_web_scraping()
        self.__dados_empresa_label_valores['Oscilacoes'] = OscilacoesEmpresaBusiness(self.__papel).iniciar_web_scraping()
        self.__dados_empresa_label_valores['Indicadores'] = IndicadoresEmpresaBusiness(self.__papel).iniciar_web_scraping()
        return self.__dados_empresa_label_valores

    def balanco_empresa_web_scraping(self):
        self.__dados_empresa_label_valores['Balanco'] = BalancoEmpresaBusiness(self.__papel).iniciar_web_scraping()
        return self.__dados_empresa_label_valores
