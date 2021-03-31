from pyspark.sql import SparkSession
from etl.fundamentus_etl import DAConexaoFactory

class DAConexaoHadoop(DAConexaoFactory):

    def __init__(self, app_name, nome_banco):
        super().__init__()
        self.__url_conexao_hadoop_hdfs = None
        try:
            self.__url_conexao_hadoop_hdfs = self._get_conexao('hdfs', nome_banco)
            self.__spark_session = SparkSession.builder.appName(app_name).getOrCreate()
        except Exception:
            self.__erro = 'Erro ao criar conexão com MongoDB'

    def get_spark_session_para_conexao(self):
        return self.__spark_session

    def get_url_conexao_hadoop_hdfs(self):
        return self.__url_conexao_hadoop_hdfs

    def get_erro(self):
        return self.__erro

