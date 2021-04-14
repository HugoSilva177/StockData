from extract_transform_load.fundamentus_etl.etl_mongodb.src.etl.DadosTransformacao import DadosTransformacao


class ProcessoETL:

    def __init__(self, hdfs_object):
        self.__hdfs_object = hdfs_object
        self.__spark_session = hdfs_object.get_spark_session_para_conexao()

    def _extrair_dados_empresa(self, dados_empresa):
        dados_label = dados_empresa['dados_label']
        dados_valores = dados_empresa['dados_valores']
        return dados_label, dados_valores

    def _transformar_dados_empresa(self, dados_label, dados_valores):
        dados_label = DadosTransformacao.remover_caracteres_especiais(dados_label)
        dados_valores = DadosTransformacao.transformar_lista_em_tuples(dados_valores)
        dados_empresa_spark_df = self.__spark_session.createDataFrame(dados_valores, dados_label)
        return dados_empresa_spark_df

    def _gravar_dados_empresa(self, dados_empresa_spark_df):
        self.__hdfs_object.escrever_dados_spark_dataframe_no_hdfs(dados_empresa_spark_df)









