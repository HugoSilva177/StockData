from web_scraping.fundamentus.src.business.empresa_business.EmpresaBusiness import EmpresaBusiness
from web_scraping.fundamentus.src.scraping.IndicadoresEmpresaScraping import IndicadoresEmpresaScraping


class IndicadoresEmpresaBusiness(EmpresaBusiness):

    def __init__(self, papel):
        super().__init__(IndicadoresEmpresaScraping(papel))
        self.__papel = papel
        self.__id_inserido_cotacao = None