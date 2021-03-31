from extract_transform_load.fundamentus_etl.src.etl.ProcessoETL import ProcessoETL
from extract_transform_load.fundamentus_etl.src.dao.mongodb.InfoEmpresaDAO import InfoEmpresaDAO
from extract_transform_load.fundamentus_etl.src.dao.hadoop_hdfs.InfoEmpresaHDFS import InfoEmpresaHDFS


class InfoEmpresaETL(ProcessoETL):
    def __init__(self, dados_empresa):
        super().__init__(InfoEmpresaDAO(), InfoEmpresaHDFS())
        self.__dados_empresa = dados_empresa

    def info_empresa_etl(self):
        info_empresa_label, info_empresa_dados = self._extrair_dados_empresa(self.__dados_empresa)
        dados_empresa_dicionario, dados_empresa_spark_df = self._transformar_dados_empresa(info_empresa_label,
                                                                                           info_empresa_dados)
        id_empresa_inserida = self._gravar_dados_empresa(dados_empresa_dicionario, dados_empresa_spark_df)
        return id_empresa_inserida

