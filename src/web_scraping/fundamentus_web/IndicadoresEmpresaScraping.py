from src.web_scraping.fundamentus_web.WebScraping import WebScraping


class IndicadoresEmpresaScraping(WebScraping):

    def __init__(self, papel):
        super().__init__(papel)
        self.__papel = papel

    def extrair_dados_label(self):
        indicador_fundamentalita_label = self.get_html_selector().xpath(
            "//table[3]//td[@class='label w2']//span[@class='txt']/text() | //table[3]//td[@class='label']//span[@class='txt']/text()").extract()
        return indicador_fundamentalita_label

    def extrair_dados_valores(self):
        indicador_fundamentalita_dados = self.get_html_selector().xpath(
            "//table[3]//td[@class='data w2']//span[@class='txt']/text() | //table[3]//td[@class='data']//span[@class='txt']/text()").extract()
        indicador_fundamentalita_dados = list(map(lambda dado: dado.replace("\n", ""), indicador_fundamentalita_dados))
        return indicador_fundamentalita_dados
