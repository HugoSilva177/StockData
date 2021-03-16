from src.web_scraping.fundamentus_web.WebScraping import WebScraping
from src.etl.DadosTransformacao import DadosTransformacao


class ExtractData(WebScraping):

    def __init__(self, papel):
        super.__init__(papel)
        self.__transform_data = DadosTransformacao()

    def extrair_data_ult_cotacao(self):
        data_ult_cotacao = self.get_html_selector().xpath(
            "//table[1]//span[@class='txt']/text() | // table[1]//span[@class='txt']/a/text()").extract()[7]
        data_ult_cotacao = self.__transform_data.validar_data(data_ult_cotacao)
        return data_ult_cotacao

    def extrair_data_ult_balanco(self):
        data_ult_balanco = self.get_html_selector().xpath(
            "//table[2]//span[@class='txt']/text()").extract()[3]
        data_ult_balanco = self.__transform_data.validar_data(data_ult_balanco)
        return data_ult_balanco


