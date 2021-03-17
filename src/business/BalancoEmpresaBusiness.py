from src.etl.BalancoEmpresaETL import BalancoEmpresaETL
from src.dao.fundamentus.BalancoEmpresaDAO import BalancoEmpresaDAO
from src.web_scraping.fundamentus_web.DataScraping import DataScraping


class BalancoEmpresaBusiness:

    def __init__(self, papel):
        self.__papel = papel

    def iniciar_web_scraping(self, id_dados_empresa):
        balanco_empresa_etl = BalancoEmpresaETL(self.__papel, id_dados_empresa)
        balanco_empresa_etl.iniciar_balanco_empresa_etl()

    @staticmethod
    def verificar_ultimo_balanco_existe(id_dados_empresa, papel):
        data_ultimo_balanco = DataScraping(papel).extrair_data_ult_balanco()
        utlimo_balanco = BalancoEmpresaDAO().buscar_balanco_empresa_por_id_empresa_data(id_dados_empresa,
                                                                                        data_ultimo_balanco)
        print(f"Data último balanço: {data_ultimo_balanco}")
        if utlimo_balanco is None:
            return True
        else:
            return False
