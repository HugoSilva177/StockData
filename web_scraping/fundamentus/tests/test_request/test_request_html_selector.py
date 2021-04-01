import pytest
from web_scraping.fundamentus.src.request.RequestHtmlSelector import RequestHtmlSelector
from web_scraping.fundamentus.src.exceptions.PapelInvalidoError import PapelInvalidoError


class TestRequestHtmlSelector:

    @pytest.fixture
    def request_html_selector(self):
        return RequestHtmlSelector()

    def test_deve_retornar_um_tipo_scrapy_selector(self, request_html_selector):
        html_selector = request_html_selector.get_html_selector('PETR4')
        assert str(type(html_selector)) == "<class 'scrapy.selector.unified.Selector'>"

    def test_deve_retornar_html_selector_com_len_acima_de_zero_se_existir_o_papel(self, request_html_selector):
        html_selector = request_html_selector.get_html_selector('PETR4')
        tamanho_html_selector = len(html_selector.xpath("//table[@class='w728']"))
        assert tamanho_html_selector > 0

    def test_deve_lancar_excecao_de_papel_invalido_caso_papel_nao_exista(self, request_html_selector):
        with pytest.raises(PapelInvalidoError):
            request_html_selector.get_html_selector('PETR')

