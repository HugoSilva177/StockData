from src.web_scraping.fundamentus_web.WebScraping import WebScraping


class CotacaoEmpresaScraping(WebScraping):

    def __init__(self, papel):
        super().__init__(papel)


    def extrair_cotacao_empresa_label(self):
        cotacao_label = self.get_html_selector().xpath(
            "//table[1]//span[@class='txt']/text() | //table[1]//span[@class='txt']/a/text()").extract()[0::2][1::2]
        cotacao_label += self.get_html_selector().xpath("//table[2]//span[@class='txt']/text()").extract()[0::2][0::3]
        return cotacao_label

    def extrair_cotacao_empresa_dados(self):
        cotacao_dados = self.get_html_selector().xpath(
            "//table[1]//span[@class='txt']/text() | //table[1]//span[@class='txt']/a/text()").extract()[1::2][1::2]
        cotacao_dados += self.get_html_selector().xpath("//table[2]//span[@class='txt']/text()").extract()[1::2][0::3]
        return cotacao_dados
