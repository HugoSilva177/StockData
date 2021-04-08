from extract_transform_load.fundamentus_etl.etl_hdfs.src.etl.ProcessoETL import ProcessoETL
from extract_transform_load.fundamentus_etl.etl_hdfs.src.dao.IndicadoresEmpresaHDFS import IndicadoresEmpresaHDFS


class IndicadoresEmpresaETL(ProcessoETL):

    def __init__(self, dados_empresa):
        super().__init__(IndicadoresEmpresaHDFS())
        self.__dados_empresa = dados_empresa

    def indicadores_empresa_etl(self):
        indicadores_empresa_label, indicadores_empresa_dados = self._extrair_dados_empresa(self.__dados_empresa)

        dados_empresa_spark_df = self._transformar_dados_empresa(indicadores_empresa_label,
                                                                 indicadores_empresa_dados)
        self._gravar_dados_empresa(dados_empresa_spark_df)


