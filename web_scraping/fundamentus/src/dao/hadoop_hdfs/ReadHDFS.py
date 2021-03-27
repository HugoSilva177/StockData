from web_scraping.fundamentus.src.connect_db.DAConexaoHadoop import DAConexaoHadoop
from abc import ABCMeta, abstractmethod


class ReadHDFS(metaclass=ABCMeta, DAConexaoHadoop):

    def __init__(self, app_name, url_complementar):
        super().__init__(app_name, url_complementar)
        self.__url_conexao_hadoop = self.get_url_conexao_hadoop_hdfs()

    def _ler_dados_spark_dataframe_no_hdfs(self):
        dados_spark_df = self.__spark_session.read.format('parquet').load(self.__url_conexao_hadoop)
        return dados_spark_df

    @abstractmethod
    def filtrar_dados_empresa(self, papel, data=None):
        return


