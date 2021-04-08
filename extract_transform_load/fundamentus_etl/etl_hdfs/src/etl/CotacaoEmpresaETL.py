from extract_transform_load.fundamentus_etl.etl_hdfs.src.etl.ProcessoETL import ProcessoETL
from extract_transform_load.fundamentus_etl.etl_hdfs.src.dao.CotacaoEmpresaHDFS import CotacaoEmpresaHDFS


class CotacaoEmpresaETL(ProcessoETL):

    def __init__(self, dados_empresa):
        super().__init__(CotacaoEmpresaHDFS())
        self.__dados_empresa = dados_empresa

    def cotacao_empresa_etl(self):
        cotacao_empresa_label, cotacao_empresa_dados = self._extrair_dados_empresa(self.__dados_empresa)
        dados_empresa_spark_df = self._transformar_dados_empresa(cotacao_empresa_label,
                                                                 cotacao_empresa_dados)
        self._gravar_dados_empresa(dados_empresa_spark_df)




