from web_scraping.fundamentus.src.business.empresa_business.EmpresaBusiness import EmpresaBusiness
from web_scraping.fundamentus.src.scraping.OscilacoesEmpresaScraping import OscilacoesEmpresaScraping
from web_scraping.fundamentus.src.business.empresa_business.CotacaoEmpresaBusiness import CotacaoEmpresaBusiness


class OscilacoesEmpresaBusiness(EmpresaBusiness):

    def __init__(self, papel):
        super().__init__(OscilacoesEmpresaScraping(papel))
        self.__papel = papel
        self.__id_inserido_cotacao = None
