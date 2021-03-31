import pytest
from etl.fundamentus_etl import InfoEmpresaScraping
from etl.fundamentus_etl import CotacaoEmpresaScraping
from etl.fundamentus_etl import OscilacoesEmpresaScraping
from etl.fundamentus_etl import IndicadoresEmpresaScraping
from etl.fundamentus_etl import BalancoEmpresaScraping


class TestInfoEmpresaScraping:

    @pytest.fixture(params=[InfoEmpresaScraping('PETR4'),
                            CotacaoEmpresaScraping('PETR4'),
                            OscilacoesEmpresaScraping('PETR4'),
                            IndicadoresEmpresaScraping('PETR4'),
                            BalancoEmpresaScraping('PETR4')])
    def dados_empresa_scraping(self, request):
        return request.param

    def test_deve_retornar_quantidade_minima_de_labels_e_de_valores(self, dados_empresa_scraping):
        quantidade_retornada_labels = len(dados_empresa_scraping.scraping_dados_label())
        quantidade_retornada_valores = len(dados_empresa_scraping.extrair_dados_valores())
        quantidade_minima = 1
        assert quantidade_retornada_labels >= quantidade_minima
        assert quantidade_retornada_valores >= quantidade_minima


    def test_deve_retornar_mesma_quantidade_labels_e_valores(self, dados_empresa_scraping):
        quantidade_labels = len(dados_empresa_scraping.scraping_dados_label())
        quantidade_valores = len(dados_empresa_scraping.extrair_dados_valores())
        assert quantidade_labels == quantidade_valores