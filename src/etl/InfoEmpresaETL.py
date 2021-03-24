from src.etl.ProcessoETL import ProcessoETL
from src.dao.fundamentus.InfoEmpresaDAO import InfoEmpresaDAO
from src.web_scraping.fundamentus_web.InfoEmpresaScraping import InfoEmpresaScraping

class InfoEmpresaETL(ProcessoETL):
    def __init__(self, papel):
        super().__init__(InfoEmpresaScraping(papel), InfoEmpresaDAO())

    def iniciar_info_empresa_etl(self):
        info_empresa_label, info_empresa_dados = self._extrair_dados_empresa(list(), list())
        dados_empresa_dicionario, dados_empresa_spark_df = self._transformar_dados_empresa(info_empresa_label, info_empresa_dados)
        id_empresa_inserida = self._gravar_dados_empresa(dados_empresa_dicionario, dados_empresa_spark_df)
        return id_empresa_inserida
