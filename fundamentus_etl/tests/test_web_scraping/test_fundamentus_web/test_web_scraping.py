from fundamentus_etl.src.web_scraping.fundamentus_web.InfoEmpresaScraping import InfoEmpresaScraping


import pytest

class TestWebScraping:

    @pytest.fixture
    def web_scraping(self):
        return InfoEmpresaScraping('PETR4')

    def test_deve_retornar_um_html_selector_valido(self, web_scraping):
        html_selector = web_scraping._get_html_selector()
        quantidade_retornada_tabelas = len(html_selector.xpath("//table[@class='w728']").extract())
        quantidade_minima_tabelas = 1
        assert quantidade_retornada_tabelas >= quantidade_minima_tabelas
