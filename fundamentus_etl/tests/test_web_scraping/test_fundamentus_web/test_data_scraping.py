import pytest
from fundamentus_etl.src.web_scraping.fundamentus_web.DataScraping import DataScraping


class TestDataScraping:

    @pytest.fixture
    def data_scraping(self):
        return DataScraping('PETR4')

    def test_deve_extrair_e_retornar_data_ult_cotacao_como_string_de_dez_caracteres(self, data_scraping):
        data_ult_cotacao_retonardo = data_scraping.extrair_data_ult_cotacao()
        assert str(type(data_ult_cotacao_retonardo)) == "<class 'str'>"
        quantidade_minima_caracteres = 10
        assert len(data_ult_cotacao_retonardo) == quantidade_minima_caracteres

    def test_deve_extrair_e_retornar_data_ult_balanco_como_string_de_dez_caracteres(self, data_scraping):
        data_ult_balanco_retonardo = data_scraping.extrair_data_ult_balanco()
        assert str(type(data_ult_balanco_retonardo)) == "<class 'str'>"
        quantidade_minima_caracteres = 10
        assert len(data_ult_balanco_retonardo) == quantidade_minima_caracteres
