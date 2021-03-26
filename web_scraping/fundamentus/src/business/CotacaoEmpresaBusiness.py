from web_scraping.fundamentus.src.business.EmpresaBusiness import EmpresaBusiness
from web_scraping.fundamentus.src.scraping.DataScraping import DataScraping
from web_scraping.fundamentus.src.dao.mongo_db.CotacaoEmpresaDAO import CotacaoEmpresaDAO
from web_scraping.fundamentus.src.scraping.CotacaoEmpresaScraping import CotacaoEmpresaScraping


class CotacaoEmpresaBusiness(EmpresaBusiness):

    def __init__(self, papel):
        super().__init__(CotacaoEmpresaScraping(papel))
        self.__papel = papel
        self.__id_inserido_cotacao = None

    @staticmethod
    def verificar_ultima_cotacao_existe_mongodb(id_dados_empresa, papel):
        data_ultima_cotacao_scraping = DataScraping(papel).extrair_data_ult_cotacao()
        print(f"Data última cotação Web Scraping: {data_ultima_cotacao_scraping}")
        ultima_cotacao_mongodb = CotacaoEmpresaDAO().buscar_cotacao_empresa_por_id_empresa_data(id_dados_empresa,
                                                                                        data_ultima_cotacao_scraping)
        print(f"Data última cotacação MongoDB: {ultima_cotacao_mongodb}")
        if ultima_cotacao_mongodb is None:
            return True
        else:
            return False