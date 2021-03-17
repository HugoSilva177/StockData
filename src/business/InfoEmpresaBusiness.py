from src.etl.InfoEmpresaETL import InfoEmpresaETL
from src.dao.fundamentus.InfoEmpresaDAO import InfoEmpresaDAO


class InfoEmpresaBusiness:

    def __init__(self, papel):
        self.__papel = papel

    def iniciar_web_scraping(self):
        info_empresa_etl = InfoEmpresaETL(self.__papel)
        id_empresa_inserida = info_empresa_etl.iniciar_info_empresa_etl()
        return id_empresa_inserida

    def info_dados_empresa_nao_exitem(self):
        dados_empresa = InfoEmpresaDAO().buscar_dados_empresa_por_papel(self.__papel)
        if dados_empresa is None:
            return True
        else:
            return False









