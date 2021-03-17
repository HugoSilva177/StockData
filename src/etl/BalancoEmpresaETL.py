from src.etl.ProcessoETL import ProcessoETL
from src.dao.fundamentus.InfoEmpresaDAO import InfoEmpresaDAO
from src.dao.fundamentus.BalancoEmpresaDAO import BalancoEmpresaDAO
from src.web_scraping.fundamentus_web.BalancoEmpresaScraping import BalancoEmpresaScraping


class BalancoEmpresaETL(ProcessoETL):

    def __init__(self, papel):
        super().__init__(BalancoEmpresaScraping(papel), BalancoEmpresaDAO())
        self.__papel = papel

    def iniciar_balanco_empresa_etl(self):
        info_empresa_dao = InfoEmpresaDAO()
        balanco_empresa_label, balanco_empresa_dados = self._extrair_dados_empresa()
        balanco_empresa = self._transformar_dados_empresa(balanco_empresa_label,
                                                          balanco_empresa_dados)
        id_empresa = info_empresa_dao.buscar_dados_empresa_por_papel(self.__papel)
        balanco_empresa['Empresa'] = id_empresa['Papel']
        self._gravar_dados_empresa_db(balanco_empresa)
