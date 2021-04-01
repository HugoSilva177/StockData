from web_scraping.fundamentus.src.scraping.WebScraping import WebScraping
from web_scraping.fundamentus.src.scraping.DataScraping import DataScraping


class IndicadoresEmpresaScraping(WebScraping):

    def __init__(self, papel, html_selector):
        super().__init__()
        self.__papel = papel
        self.__html_selector = html_selector

    def scraping_dados_label(self):
        indicador_fundamentalita_label = self.__html_selector.xpath(
            "//table[3]//td[@class='label w2']//span[@class='txt']/text() | "
            "//table[3]//td[@class='label']//span[@class='txt']/text()").extract()
        indicador_fundamentalita_label.insert(0, 'Data_ult_cot')
        indicador_fundamentalita_label.insert(0, 'Papel')
        return indicador_fundamentalita_label

    def scraping_dados_valores(self):
        data_ult_cotacao = DataScraping(self.__html_selector).extrair_data_ult_cotacao()
        indicador_fundamentalita_dados = self.__html_selector.xpath(
            "//table[3]//td[@class='data w2']//span[@class='txt']/text() | "
            "//table[3]//td[@class='data']//span[@class='txt']/text()").extract()
        indicador_fundamentalita_dados = list(map(lambda dado: dado.replace("\n", ""), indicador_fundamentalita_dados))
        indicador_fundamentalita_dados.insert(0, data_ult_cotacao)
        indicador_fundamentalita_dados.insert(0, self.__papel)
        return indicador_fundamentalita_dados
