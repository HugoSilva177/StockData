import pytest
from web_scraping.fundamentus.src.dao.hadoop_hdfs.InfoEmpresaHDFS import InfoEmpresaHDFS
from web_scraping.fundamentus.src.dao.hadoop_hdfs.CotacaoEmpresaHDFS import CotacaoEmpresaHDFS
from web_scraping.fundamentus.src.dao.hadoop_hdfs.OscilacoesEmpresaHDFS import OscilacoesEmpresaHDFS
from web_scraping.fundamentus.src.dao.hadoop_hdfs.IndicadoresEmpresaHDFS import IndicadoresEmpresaHDFS
from web_scraping.fundamentus.src.dao.hadoop_hdfs.BalancoEmpresaHDFS import BalancoEmpresaHDFS


class TestDadosEmpresaHDFS:

    @pytest.fixture
    def info_empresa_hdfs(self):
        return InfoEmpresaHDFS()

    @pytest.fixture(params=[CotacaoEmpresaHDFS(),
                            OscilacoesEmpresaHDFS(),
                            IndicadoresEmpresaHDFS()])
    def cotacao_empresa_hdfs(self, request):
        return request.param

    @pytest.fixture
    def balanco_empresa_hdfs(self):
        return BalancoEmpresaHDFS()

    def test_deve_ler_dados_no_hdfs_e_retornar_um_tipo_spark_dataframe(self, info_empresa_hdfs):
        dados_spark_df = info_empresa_hdfs._ler_dados_spark_dataframe_no_hdfs( )
        assert str(type(dados_spark_df)) == "<class 'pyspark.sql.dataframe.DataFrame'>"

    def test_deve_buscar_info_da_empresa_no_hdfs_por_papel(self, info_empresa_hdfs):
        dados_retornado = info_empresa_hdfs.buscar_dados_empresa("PETR4")
        assert len(dados_retornado) >= 1

    def test_deve_buscar_cotacao_da_empresa_no_hdfs_por_papel_e_data(self, cotacao_empresa_hdfs):
        dados_retornado = cotacao_empresa_hdfs.buscar_dados_empresa("PETR4", "05/04/2021")
        assert len(dados_retornado) >= 1

    def test_deve_buscar_balanco_da_empresa_no_hdfs_por_papel_e_data(self, balanco_empresa_hdfs):
        dados_retornado = balanco_empresa_hdfs.buscar_dados_empresa("PETR4", "31/12/2020")
        assert len(dados_retornado) >= 1

