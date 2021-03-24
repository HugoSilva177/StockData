from src.dao.hadoop_hdfs.WriteReadHDFS import WriteReadHDFS
from pyspark.sql import SparkSession


class IndicadoresEmpresaHDFS(WriteReadHDFS):

    def __init__(self):
        self.__app_name = "write_read_fundamentus_hdfs"
        self.__url_complementar = "fundamentus/detalhes/indicadores_empresa"
        super().__init__(self.__app_name, self.__url_complementar)
