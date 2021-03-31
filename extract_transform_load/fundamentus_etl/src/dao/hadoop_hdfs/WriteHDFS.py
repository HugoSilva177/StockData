from extract_transform_load.fundamentus_etl.src.connect_db.DAConexaoHadoop import DAConexaoHadoop


class WriteReadHDFS(DAConexaoHadoop):

    def __init__(self, app_name, url_complementar):
        super().__init__(app_name, url_complementar)
        self.__url_conexao_hadoop = self.get_url_conexao_hadoop_hdfs()

    def escrever_dados_spark_dataframe_no_hdfs(self, dados_spark_df):
        dados_spark_df.write.save(self.__url_conexao_hadoop, format='parquet', mode='append')



