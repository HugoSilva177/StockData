from src.etl.InfoEmpresaETL import InfoEmpresaETL


class InfoEmpresaBusiness:

    def __init__(self, papel):
        self.__papel = papel

    def iniciar_web_scraping(self):
        info_empresa_etl = InfoEmpresaETL(self.__papel)
        id_empresa_inserida = info_empresa_etl.iniciar_info_empresa_etl()

        return id_empresa_inserida






