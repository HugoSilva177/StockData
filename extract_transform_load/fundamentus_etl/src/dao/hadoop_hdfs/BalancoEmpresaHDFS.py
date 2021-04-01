from extract_transform_load.fundamentus_etl.src.dao.hadoop_hdfs.WriteHDFS import WriteReadHDFS


class BalancoEmpresaHDFS(WriteReadHDFS):

    def __init__(self):
        self.__app_name = "write_read_fundamentus_hdfs"
        self.__url_complementar = "fundamentus/detalhes/balanco_empresa"
        super().__init__(self.__app_name, self.__url_complementar)