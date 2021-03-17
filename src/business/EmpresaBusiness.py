from src.business.InfoEmpresaBusiness import InfoEmpresaBusiness
from src.business.CotacaoEmpresaBusiness import CotacaoEmpresaBusiness
from src.business.BalancoEmpresaBusiness import BalancoEmpresaBusiness


class EmpresaBusiness:

    def __init__(self, papel):
        self.__cotacao_empresa_business = None
        self.__papel = papel


    def fundamentus_web_scraping(self):
        info_empresa = InfoEmpresaBusiness(self.__papel)

        if info_empresa.info_dados_empresa_nao_exitem():
            id_empresa_inserida = info_empresa.iniciar_web_scraping()
            CotacaoEmpresaBusiness(self.__papel, id_empresa_inserida).iniciar_web_scraping()
            BalancoEmpresaBusiness(self.__papel).iniciar_web_scraping()






