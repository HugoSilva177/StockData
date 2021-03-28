from web_scraping.fundamentus.src.dao.hadoop_hdfs.ReadHDFS import ReadHDFS


class CotacaoEmpresaHDFS(ReadHDFS):

    def __init__(self):
        self.__app_name = "write_read_fundamentus_hdfs"
        self.__url_complementar = "fundamentus/detalhes/dados_cotacao"
        super().__init__(self.__app_name, self.__url_complementar)

    def buscar_dados_empresa(self, papel, data=None):
        dados_spark_df = self._ler_dados_spark_dataframe_no_hdfs()
        filtro_papel = "Papel == '%s'" % papel
        filtro_data = "Data_ult_cot == '%s'" % data
        cotacao_empresa = dados_spark_df.filter(filtro_papel).filter(filtro_data).collect()
        return cotacao_empresa
