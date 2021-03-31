from etl.fundamentus_etl import DAConexaoHadoop


class WriteReadHDFS(DAConexaoHadoop):

    def __init__(self, app_name, url_complementar):
        super().__init__(app_name, url_complementar)
        self.__url_conexao_hadoop = self.get_url_conexao_hadoop_hdfs()

    def escrever_dados_spark_dataframe_no_hdfs(self, dados_spark_df):
        dados_spark_df.write.save(self.__url_conexao_hadoop, format='parquet', mode='append')

    def ler_dados_spark_dataframe_no_hdfs(self):
        dados_spark_df = self.__spark_session.read.format('parquet').load(self.__url_conexao_hadoop)
        return dados_spark_df

