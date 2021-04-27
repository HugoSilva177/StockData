import pytest
from web_scraping.fundamentus.src.connect_db.DAConexaoHadoop import DAConexaoHadoop


class TestDAConexaoHadoop:

    @pytest.fixture
    def da_conexao_hadoop(self):
        return DAConexaoHadoop(app_name="write_read_fundamentus_hdfs")

    @pytest.fixture
    def url_hdfs_info_empresa(self):
        return "fundamentus/detalhes/info_empresa"

    @pytest.fixture
    def url_hdfs_cotacao_empresa(self):
        return "fundamentus/detalhes/cotacao_empresa"

    @pytest.fixture
    def url_hdfs_oscilacoes_empresa(self):
        return "fundamentus/detalhes/oscilacoes_empresa"

    @pytest.fixture
    def url_hdfs_indicadores_empresa(self):
        return "fundamentus/detalhes/indicadores_empresa"

    @pytest.fixture
    def url_hdfs_balanco_empresa(self):
        return "fundamentus/detalhes/balanco_empresa"


    def test_deve_retornar_um_tipo_spark_session(self, da_conexao_hadoop):
        retorno_conexao_hadoop = da_conexao_hadoop.get_spark_session_para_conexao()
        assert str(type(retorno_conexao_hadoop)) == "<class 'pyspark.sql.session.SparkSession'>"

    def test_deve_retornar_url_hdfs_info_empresa(self, da_conexao_hadoop, url_hdfs_info_empresa):
        retorno_url_hdfs = da_conexao_hadoop.get_url_conexao_hadoop_hdfs(url_hdfs_info_empresa)
        assert retorno_url_hdfs == "hdfs://172.17.177.40:9000/user/hadoopuser/fundamentus/detalhes/info_empresa"

    def test_deve_retornar_url_hdfs_cotacao_empresa(self, da_conexao_hadoop, url_hdfs_cotacao_empresa):
        retorno_url_hdfs = da_conexao_hadoop.get_url_conexao_hadoop_hdfs(url_hdfs_cotacao_empresa)
        assert retorno_url_hdfs == "hdfs://172.17.177.40:9000/user/hadoopuser/fundamentus/detalhes/cotacao_empresa"

    def test_deve_retornar_url_hdfs_oscilacoes_empresa(self, da_conexao_hadoop, url_hdfs_oscilacoes_empresa):
        retorno_url_hdfs = da_conexao_hadoop.get_url_conexao_hadoop_hdfs(url_hdfs_oscilacoes_empresa)
        assert retorno_url_hdfs == "hdfs://172.17.177.40:9000/user/hadoopuser/fundamentus/detalhes/oscilacoes_empresa"

    def test_deve_retornar_url_hdfs_indicadores_empresa(self, da_conexao_hadoop, url_hdfs_indicadores_empresa):
        retorno_url_hdfs = da_conexao_hadoop.get_url_conexao_hadoop_hdfs(url_hdfs_indicadores_empresa)
        assert retorno_url_hdfs == "hdfs://172.17.177.40:9000/user/hadoopuser/fundamentus/detalhes/indicadores_empresa"

    def test_deve_retornar_url_hdfs_balanco_empresa(self, da_conexao_hadoop, url_hdfs_balanco_empresa):
        retorno_url_hdfs = da_conexao_hadoop.get_url_conexao_hadoop_hdfs(url_hdfs_balanco_empresa)
        assert retorno_url_hdfs == "hdfs://172.17.177.40:9000/user/hadoopuser/fundamentus/detalhes/balanco_empresa"
