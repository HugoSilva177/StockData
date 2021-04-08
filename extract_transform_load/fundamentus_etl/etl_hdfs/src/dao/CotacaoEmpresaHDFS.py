from extract_transform_load.fundamentus_etl.etl_hdfs.src.dao.WriteHDFS import WriteReadHDFS


class CotacaoEmpresaHDFS(WriteReadHDFS):

    def __init__(self):
        self.__app_name = "write_read_fundamentus_hdfs"
        self.__url_complementar = "fundamentus/detalhes/cotacao_empresa"
        super().__init__(self.__app_name, self.__url_complementar)

