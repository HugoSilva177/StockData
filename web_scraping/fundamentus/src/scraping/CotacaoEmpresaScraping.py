from web_scraping.fundamentus.src.scraping.WebScraping import WebScraping


class CotacaoEmpresaScraping(WebScraping):

    def __init__(self, papel, html_selector):
        super().__init__()
        self.__papel = papel
        self.__html_selector = html_selector

    def scraping_dados_label(self):
        cotacao_label = self.__html_selector.xpath(
            "//table[1]//span[@class='txt']/text() | //table[1]//span[@class='txt']/a/text()").extract()[0::2][1::2]
        cotacao_label += self.__html_selector.xpath("//table[2]//span[@class='txt']/text()").extract()[0::2][0::3]
        cotacao_label.insert(0, 'Papel')
        return cotacao_label

    def extrair_dados_valores(self):
        cotacao_dados = self.__html_selector.xpath(
            "//table[1]//span[@class='txt']/text() | //table[1]//span[@class='txt']/a/text()").extract()[1::2][1::2]
        cotacao_dados += self.__html_selector.xpath("//table[2]//span[@class='txt']/text()").extract()[1::2][0::3]
        cotacao_dados.insert(0, self.__papel)
        return cotacao_dados
