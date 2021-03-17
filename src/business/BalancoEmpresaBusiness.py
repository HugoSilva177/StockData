from src.etl.BalancoEmpresaETL import BalancoEmpresaETL
from src.dao.fundamentus.BalancoEmpresaDAO import BalancoEmpresaDAO
from src.web_scraping.fundamentus_web.DataScraping import DataScraping


class BalancoEmpresaBusiness:

    def __init__(self, papel):
        self.__papel = papel

    def iniciar_web_scraping(self):
        balanco_empresa_etl = BalancoEmpresaETL(self.__papel)
        balanco_empresa_etl.iniciar_balanco_empresa_etl()

    def ultimo_balanco_nao_existe(self):
        data_ultimo_balanco = DataScraping(self.__papel).extrair_data_ult_balanco()
        utlimo_balanco = BalancoEmpresaDAO().buscar_lista_balancos_empresa_por_papel_data(self.__papel, data_ultimo_balanco)
        if utlimo_balanco is None:
            return True
        else:
            return False
