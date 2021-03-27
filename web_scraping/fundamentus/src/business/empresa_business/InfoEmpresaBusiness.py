from web_scraping.fundamentus.src.dao.mongo_db.InfoEmpresaDAO import InfoEmpresaDAO
from web_scraping.fundamentus.src.dao.hadoop_hdfs.InfoEmpresaHDFS import InfoEmpresaHDFS
from web_scraping.fundamentus.src.scraping.InfoEmpresaScraping import InfoEmpresaScraping
from web_scraping.fundamentus.src.business.empresa_business.EmpresaBusiness import EmpresaBusiness


class InfoEmpresaBusiness(EmpresaBusiness):

    def __init__(self, papel):
        super().__init__(InfoEmpresaScraping(papel))
        self.__papel = papel

    @staticmethod
    def verificar_dados_empresa_exitem_mongodb(papel):
        dados_empresa = InfoEmpresaDAO().buscar_dados_empresa(papel)
        if dados_empresa is None:
            return None
        else:
            return dados_empresa['_id']

    @staticmethod
    def verificar_dados_empresa_exitem_hdfs(papel):
        dados_empresa = InfoEmpresaHDFS().filtrar_dados_empresa(papel)
        if len(dados_empresa) == 0:
            return None
        else:
            return dados_empresa['_id']








