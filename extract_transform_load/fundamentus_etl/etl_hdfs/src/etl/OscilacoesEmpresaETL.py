from extract_transform_load.fundamentus_etl.etl_hdfs.src.etl.ProcessoETL import ProcessoETL
from extract_transform_load.fundamentus_etl.etl_hdfs.src.dao.OscilacoesEmpresaHDFS import OscilacoesEmpresaHDFS


class OscilacoesEmpresaETL(ProcessoETL):

    def __init__(self, dados_empresa):
        super().__init__(OscilacoesEmpresaHDFS())
        self.__dados_empresa = dados_empresa


    def oscilacoes_empresa_etl(self):
        oscilacoes_empresa_label, oscilacoes_empresa_dados = self._extrair_dados_empresa(self.__dados_empresa)

        dados_empresa_spark_df = self._transformar_dados_empresa(oscilacoes_empresa_label,
                                                                 oscilacoes_empresa_dados)
        self._gravar_dados_empresa(dados_empresa_spark_df)



