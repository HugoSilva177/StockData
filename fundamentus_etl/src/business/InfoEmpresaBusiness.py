from fundamentus_etl.src.etl import InfoEmpresaETL
from fundamentus_etl.src.dao.mongodb.InfoEmpresaDAO import InfoEmpresaDAO


class InfoEmpresaBusiness:

    def __init__(self, papel):
        self.__papel = papel

    def iniciar_web_scraping(self):
        info_empresa_etl = InfoEmpresaETL(self.__papel)
        id_empresa_inserida = info_empresa_etl.iniciar_info_empresa_etl()
        return id_empresa_inserida

    @staticmethod
    def verificar_dados_empresa_exitem(papel):
        dados_empresa = InfoEmpresaDAO().buscar_dados_empresa_por_papel(papel)
        if dados_empresa is None:
            return None
        else:
            return dados_empresa['_id']









