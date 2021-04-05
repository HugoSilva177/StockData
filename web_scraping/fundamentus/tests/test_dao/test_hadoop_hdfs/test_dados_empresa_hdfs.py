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
                            IndicadoresEmpresaHDFS(),
                            BalancoEmpresaHDFS()])
    def cotacao_balanco_empresa_hdfs(self, request):
        return request.param

    def test_deve_buscar_info_da_empresa_no_hdfs_por_papel(self, info_empresa_hdfs):
        dados_retornado = info_empresa_hdfs.buscar_dados_empresa("PETR4")
        assert dados_retornado == ""

    def test_deve_buscar_cotacao_balanco_da_empresa_no_hdfs_por_papel_e_data(self, cotacao_balanco_empresa_hdfs):
        dados_retornado = cotacao_balanco_empresa_hdfs.buscar_dados_empresa("PETR4", "01/04/2021")
        assert dados_retornado == ""
