from src.web_scraping.fundamentus_web.WebScraping import WebScraping


class OscilacoesEmpresaScraping(WebScraping):

    def __init__(self, papel):
        super().__init__(papel)

    def extrair_dados_label(self):
        oscilacao_label = self._get_html_selector().xpath(
            "//table[3]//td[@class='nivel1']//span/text()").extract()[0]
        lista_oscilacoes_label = self._get_html_selector().xpath(
            "//table[3]//td[@class='label w1']//span/text()").extract()
        oscilacoes_label = list(map(lambda label: oscilacao_label + "_" + label, lista_oscilacoes_label))
        return oscilacoes_label

    def extrair_dados_valores(self):
        oscilacoes_dados = self._get_html_selector().xpath(
            "//table[3]//span[@class='oscil']/font/text()").extract()
        return oscilacoes_dados
