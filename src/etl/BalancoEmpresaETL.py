from src.etl.ProcessoETL import ProcessoETL
from src.dao.fundamentus.InfoEmpresaDAO import InfoEmpresaDAO
from src.dao.fundamentus.BalancoEmpresaDAO import BalancoEmpresaDAO
from src.web_scraping.fundamentus_web.BalancoEmpresaScraping import BalancoEmpresaScraping


class BalancoEmpresaETL(ProcessoETL):

    def __init__(self, papel, id_dados_empresa):
        super().__init__(BalancoEmpresaScraping(papel), BalancoEmpresaDAO())
        self.__id_dados_empresa = id_dados_empresa

    def iniciar_balanco_empresa_etl(self):
        balanco_empresa_label, balanco_empresa_dados = self._extrair_dados_empresa()
        balanco_empresa = self._transformar_dados_empresa(balanco_empresa_label,
                                                          balanco_empresa_dados)
        balanco_empresa['Empresa'] = self.__id_dados_empresa
        self._gravar_dados_empresa_db(balanco_empresa)
