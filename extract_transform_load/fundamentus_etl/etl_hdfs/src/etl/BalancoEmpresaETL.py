from extract_transform_load.fundamentus_etl.etl_hdfs.src.etl.ProcessoETL import ProcessoETL
from extract_transform_load.fundamentus_etl.etl_hdfs.src.dao.BalancoEmpresaHDFS import BalancoEmpresaHDFS


class BalancoEmpresaETL(ProcessoETL):

    def __init__(self, dados_empresa):
        super().__init__(BalancoEmpresaHDFS())
        self.__dados_empresa = dados_empresa

    def balanco_empresa_etl(self):
        balanco_empresa_label, balanco_empresa_dados = self._extrair_dados_empresa(self.__dados_empresa)
        dados_empresa_spark_df = self._transformar_dados_empresa(balanco_empresa_label,
                                                                 balanco_empresa_dados)
        self._gravar_dados_empresa(dados_empresa_spark_df)
