from web_scraping.fundamentus.src.business.EmpresaBusiness import EmpresaBusiness
from web_scraping.fundamentus.src.scraping.BalancoEmpresaScraping import BalancoEmpresaScraping


from fundamentus_etl.src.etl.BalancoEmpresaETL import BalancoEmpresaETL
from fundamentus_etl.src.dao.mongodb.BalancoEmpresaDAO import BalancoEmpresaDAO
from fundamentus_etl.src.web_scraping.fundamentus_web.DataScraping import DataScraping


class BalancoEmpresaBusiness(EmpresaBusiness):

    def __init__(self, papel):
        super().__init__(BalancoEmpresaScraping(papel))
        self.__papel = papel

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
