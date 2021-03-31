from web_scraping.fundamentus.src.dao.hadoop_hdfs.ReadHDFS import ReadHDFS


class BalancoEmpresaHDFS(ReadHDFS):

    def __init__(self):
        self.__app_name = "write_read_fundamentus_hdfs"
        self.__url_complementar = "fundamentus/detalhes/balanco_empresa"
        super().__init__(self.__app_name, self.__url_complementar)

    def buscar_dados_empresa(self, papel, data=None):
        dados_spark_df = self._ler_dados_spark_dataframe_no_hdfs()
        filtro_papel = "Papel == '%s'" % papel
        filtro_data = "Ult_balanco_processado == '%s'" % data
        balanco_empresa = dados_spark_df.filter(filtro_papel).filter(filtro_data).collect()
        return balanco_empresa
