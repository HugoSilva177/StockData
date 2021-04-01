import pytest
from web_scraping.fundamentus.src.request.RequestHtmlSelector import RequestHtmlSelector
from web_scraping.fundamentus.src.scraping.InfoEmpresaScraping import InfoEmpresaScraping
from web_scraping.fundamentus.src.scraping.CotacaoEmpresaScraping import CotacaoEmpresaScraping
from web_scraping.fundamentus.src.scraping.BalancoEmpresaScraping import BalancoEmpresaScraping
from web_scraping.fundamentus.src.scraping.OscilacoesEmpresaScraping import OscilacoesEmpresaScraping
from web_scraping.fundamentus.src.scraping.IndicadoresEmpresaScraping import IndicadoresEmpresaScraping


class TestInfoEmpresaScraping:

    __html_selector = RequestHtmlSelector().get_html_selector('PETR4')

    @pytest.fixture(params=[InfoEmpresaScraping(__html_selector),
                            CotacaoEmpresaScraping('PETR4', __html_selector),
                            OscilacoesEmpresaScraping('PETR4', __html_selector),
                            IndicadoresEmpresaScraping('PETR4', __html_selector),
                            BalancoEmpresaScraping('PETR4', __html_selector)])
    def dados_empresa_scraping(self, request):
        return request.param

    def test_deve_retornar_quantidade_minima_de_labels_e_de_valores(self, dados_empresa_scraping):
        quantidade_retornada_labels = len(dados_empresa_scraping.scraping_dados_label())
        quantidade_retornada_valores = len(dados_empresa_scraping.scraping_dados_valores())
        quantidade_minima = 1
        assert quantidade_retornada_labels >= quantidade_minima
        assert quantidade_retornada_valores >= quantidade_minima

    def test_deve_retornar_mesma_quantidade_labels_e_valores(self, dados_empresa_scraping):
        quantidade_labels = len(dados_empresa_scraping.scraping_dados_label())
        quantidade_valores = len(dados_empresa_scraping.scraping_dados_valores())
        assert quantidade_labels == quantidade_valores
