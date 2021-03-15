from src.web_scraping.fundamentus_web.WebScraping import WebScraping


class InfoEmpresaScraping(WebScraping):

    def __init__(self, papel):
        super().__init__(papel)


    def extrair_info_empresa_label(self):
        info_empresa_label = self.get_html_selector().xpath(
            "//table[1]//span[@class='txt']/text() | //table[1]//span[@class='txt']/a/text()").extract()[0::2][0::2]
        return info_empresa_label

    def extrair_info_empresa_dados(self):
        info_empresa_dados = self.get_html_selector().xpath(
            "//table[1]//span[@class='txt']/text() | //table[1]//span[@class='txt']/a/text()").extract()[1::2][0::2]
        return info_empresa_dados
