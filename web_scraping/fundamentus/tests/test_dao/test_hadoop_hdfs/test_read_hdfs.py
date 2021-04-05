import pytest
from web_scraping.fundamentus.src.dao.hadoop_hdfs.ReadHDFS import ReadHDFS


class TestReadHDFS:

    @pytest.fixture
    def instancia_read_hdfs(self):
        app_name = "write_read_fundamentus_hdfs"
        url_complementar = "fundamentus/detalhes/info_empresa"
        return ReadHDFS(app_name, url_complementar)

    def test_deve_ler_dados_no_hdfs_e_retornar_um_tipo_spark_dataframe(self, instancia_read_hdfs):
        dados_spark_df = instancia_read_hdfs._ler_dados_spark_dataframe_no_hdfs()
        assert str(type(dados_spark_df)) == ""