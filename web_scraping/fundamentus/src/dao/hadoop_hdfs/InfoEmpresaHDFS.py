from web_scraping.fundamentus.src.dao.hadoop_hdfs.ReadHDFS import ReadHDFS


class InfoEmpresaHDFS(ReadHDFS):

    def __init__(self, url_complementar="fundamentus/detalhes/info_empresa"):
        self.__app_name = "write_read_fundamentus_hdfs"
        super().__init__(self.__app_name, url_complementar)

    def buscar_dados_empresa(self, papel, data_cotacao=None):
        dados_spark_df = self._ler_dados_spark_dataframe_no_hdfs()
        if dados_spark_df is None:
            return None
        filtro_papel = "Papel == '%s'" % papel
        info_empresa = dados_spark_df.filter(filtro_papel).collect()
        return info_empresa
