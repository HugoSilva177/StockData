from src.web_scraping.fundamentus_web.WebScraping import WebScraping


class DataScraping(WebScraping):

    def __init__(self, papel):
        super().__init__(papel)

    def extrair_data_ult_cotacao(self):
        data_ult_cotacao = self._get_html_selector().xpath(
            "//table[1]//span[@class='txt']/text() | // table[1]//span[@class='txt']/a/text()").extract()[7]
        return data_ult_cotacao

    def extrair_data_ult_balanco(self):
        data_ult_balanco = self._get_html_selector().xpath(
            "//table[2]//span[@class='txt']/text()").extract()[3]
        return data_ult_balanco

    def extrair_dados_label(self):
        return

    def extrair_dados_valores(self):
        return


