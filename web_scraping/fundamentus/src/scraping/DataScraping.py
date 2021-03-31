
class DataScraping:

    def __init__(self, html_selector):
        self.__html_selector = html_selector

    def extrair_data_ult_cotacao(self):
        data_ult_cotacao = self.__html_selector.xpath(
            "//table[1]//span[@class='txt']/text() | // table[1]//span[@class='txt']/a/text()").extract()[7]
        return data_ult_cotacao

    def extrair_data_ult_balanco(self):
        data_ult_balanco = self.__html_selector.xpath(
            "//table[2]//span[@class='txt']/text()").extract()[3]
        return data_ult_balanco



