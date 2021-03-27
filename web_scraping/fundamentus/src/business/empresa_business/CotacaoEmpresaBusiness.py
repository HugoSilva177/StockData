from web_scraping.fundamentus.src.business.empresa_business.EmpresaBusiness import EmpresaBusiness
from web_scraping.fundamentus.src.scraping.DataScraping import DataScraping
from web_scraping.fundamentus.src.dao.mongo_db.CotacaoEmpresaDAO import CotacaoEmpresaDAO
from web_scraping.fundamentus.src.scraping.CotacaoEmpresaScraping import CotacaoEmpresaScraping
from web_scraping.fundamentus.src.dao.hadoop_hdfs.CotacaoEmpresaHDFS import CotacaoEmpresaHDFS


class CotacaoEmpresaBusiness(EmpresaBusiness):

    def __init__(self, papel):
        super().__init__(CotacaoEmpresaScraping(papel))

    @staticmethod
    def verificar_ultima_cotacao_existe_mongodb(papel):
        data_ultima_cotacao_scraping = DataScraping(papel).extrair_data_ult_cotacao()
        print(f"Data última cotação Web Scraping: {data_ultima_cotacao_scraping}")
        ultima_cotacao_mongodb = CotacaoEmpresaDAO().buscar_dados_empresa(papel,
                                                                          data_ultima_cotacao_scraping)
        print(f"Data última cotacação MongoDB: {ultima_cotacao_mongodb}")
        if ultima_cotacao_mongodb is None:
            return True
        else:
            return False

    @staticmethod
    def verificar_ultima_cotacao_existe_hdfs(papel):
        data_ultima_cotacao_scraping = DataScraping(papel).extrair_data_ult_cotacao()
        print(f"Data última cotação Web Scraping: {data_ultima_cotacao_scraping}")
        ultima_cotacao_hdfs = CotacaoEmpresaHDFS().filtrar_dados_empresa(papel,
                                                                         data_ultima_cotacao_scraping)
        print(f"Data última cotacação MongoDB: {ultima_cotacao_hdfs}")
        if len(ultima_cotacao_hdfs) == 0:
            return True
        else:
            return False

