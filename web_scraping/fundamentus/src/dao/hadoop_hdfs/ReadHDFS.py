from abc import ABCMeta, abstractmethod
from pyspark.sql.utils import AnalysisException
from web_scraping.fundamentus.src.connect_db.DAConexaoHadoop import DAConexaoHadoop


class ReadHDFS(metaclass=ABCMeta):

    def __init__(self, app_name, url_complementar):
        self.__conexao_hadoop = DAConexaoHadoop(app_name)
        self.__spark_session = self.__conexao_hadoop.get_spark_session_para_conexao()
        self.__url_conexao_hadoop = self.__conexao_hadoop.get_url_conexao_hadoop_hdfs(url_complementar)

    def _ler_dados_spark_dataframe_no_hdfs(self):
        try:
            dados_spark_df = self.__spark_session.read.format('parquet').load(self.__url_conexao_hadoop)
            return dados_spark_df
        except AnalysisException:
            print("Diretório ainda não existe no HDFS!")
            return None

    @abstractmethod
    def buscar_dados_empresa(self, papel, data=None):
        return


