from pyspark.sql import SparkSession
from web_scraping.fundamentus.src.connect_db.DAConexaoFactory import DAConexaoFactory


class DAConexaoHadoop(DAConexaoFactory):

    def __init__(self, app_name):
        super().__init__()
        try:
            self.__spark_session = SparkSession.builder.appName(app_name).getOrCreate()
        except Exception:
            self.__erro = 'Erro ao criar SparkSession no Hadoop'

    def get_spark_session_para_conexao(self):
        return self.__spark_session

    def get_url_conexao_hadoop_hdfs(self, nome_banco):
        url_conexao_hadoop_hdfs = self._get_conexao('hdfs', nome_banco)
        return url_conexao_hadoop_hdfs

    def get_erro(self):
        return self.__erro
