from web_scraping.fundamentus.src.scraping.DataScraping import DataScraping
from web_scraping.fundamentus.src.business.empresa_business.EmpresaBusiness import EmpresaBusiness
from web_scraping.fundamentus.src.dao.mongo_db.BalancoEmpresaDAO import BalancoEmpresaDAO
from web_scraping.fundamentus.src.dao.hadoop_hdfs.BalancoEmpresaHDFS import BalancoEmpresaHDFS
from web_scraping.fundamentus.src.scraping.BalancoEmpresaScraping import BalancoEmpresaScraping


class BalancoEmpresaBusiness(EmpresaBusiness):

    def __init__(self, papel):
        super().__init__(BalancoEmpresaScraping(papel))
        self.__papel = papel

    @staticmethod
    def verificar_ultimo_balanco_existe_mongodb(papel):
        data_ultimo_balanco = DataScraping(papel).extrair_data_ult_balanco()
        utlimo_balanco = BalancoEmpresaDAO().buscar_dados_empresa(papel, data_ultimo_balanco)
        print(f"Data último balanço: {data_ultimo_balanco}")
        if utlimo_balanco is None:
            return True
        else:
            return False

    @staticmethod
    def verificar_ultimo_balanco_existe_hdfs(papel):
        data_ultimo_balanco = DataScraping(papel).extrair_data_ult_balanco()
        print(f"Data última cotação Web Scraping: {data_ultimo_balanco}")
        ultimo_balanco_hdfs = BalancoEmpresaHDFS().filtrar_dados_empresa(papel,
                                                                         data_ultimo_balanco)
        print(f"Data última cotacação MongoDB: {ultimo_balanco_hdfs}")
        if len(ultimo_balanco_hdfs) == 0:
            return True
        else:
            return False
