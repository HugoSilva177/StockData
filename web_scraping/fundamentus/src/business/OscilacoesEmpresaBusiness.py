from web_scraping.fundamentus.src.business.EmpresaBusiness import EmpresaBusiness
from web_scraping.fundamentus.src.scraping.OscilacoesEmpresaScraping import OscilacoesEmpresaScraping


class OscilacoesEmpresaBusiness(EmpresaBusiness):

    def __init__(self, papel):
        super().__init__(OscilacoesEmpresaScraping(papel))
        self.__papel = papel
        self.__id_inserido_cotacao = None
