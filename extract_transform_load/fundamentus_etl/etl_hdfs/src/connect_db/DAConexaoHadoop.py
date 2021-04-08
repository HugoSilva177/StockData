from pyspark.sql import SparkSession


class DAConexaoHadoop:

    def __init__(self, app_name, nome_banco):
        self.__nome_banco = nome_banco
        self.__spark_session = SparkSession.builder.appName(app_name).getOrCreate()
        self.__erro = None

    def get_spark_session_para_conexao(self):
        return self.__spark_session

    def get_url_conexao_hadoop_hdfs(self):
        url_conexao_hadoop_hdfs = self.__get_conexao('hdfs', self.__nome_banco)
        return url_conexao_hadoop_hdfs

    def __get_conexao(self, banco_tipo, banco_nome):
        url_conexao = 'hdfs://172.17.177.40:9000/user/hadoopuser/'
        try:
            conexao_db = url_conexao + banco_nome
            return conexao_db
        except Exception:
            self.__erro_conexao = 'Erro ao conectar no Cluster Hadoop'

    def get_erro(self):
        return self.__erro