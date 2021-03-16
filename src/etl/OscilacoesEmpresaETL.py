from src.etl.DadosTransformacao import DadosTransformacao
from src.dao.fundamentus.OscilacoesEmpresaDAO import OscilacoesEmpresaDAO
from src.web_scraping.fundamentus_web.OscilacoesEmpresaScraping import OscilacoesEmpresaScraping
from src.etl.ProcessoETL import ProcessoETL


class OscilacoesEmpresaETL(ProcessoETL):

    def __init__(self, papel, id_inserido_cotacao):
        super().__init__(OscilacoesEmpresaScraping(papel), OscilacoesEmpresaDAO(id_inserido_cotacao))
        self.__papel = papel
        self.__id_inserido_cotacao = id_inserido_cotacao


    def iniciar_oscilacoes_etl(self):
        oscilacoes_empresa_label, oscilacoes_empresa_dados = self._extrair_dados_empresa()
        oscilacoes_empresa = self._transformar_dados_empresa(oscilacoes_empresa_label, oscilacoes_empresa_dados)
        oscilacoes_empresa['Cotacao'] = self.__id_inserido_cotacao
        self._gravar_dados_empresa_db(oscilacoes_empresa)
