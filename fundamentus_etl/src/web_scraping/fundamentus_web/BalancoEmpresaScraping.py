from fundamentus_etl.src.web_scraping.fundamentus_web.WebScraping import WebScraping


class BalancoEmpresaScraping(WebScraping):

    def __init__(self, papel):
        super().__init__(papel)

    def extrair_dados_label(self):
        balanco_label = self._get_html_selector().xpath(
            "//table[2]//span[@class='txt']/text()").extract()[2:6][0::2]
        balanco_label += self._get_html_selector().xpath(
            "//table[4]//td[@class='label w2']//span[@class='txt']/text() | "
            "//table[4]//td[@class='label']//span[@class='txt']/text()").extract()
        dre_12_meses = self._get_html_selector().xpath(
            "//table[5]//td[@class='label w2']//span[@class='txt']/text() | "
            "//table[5]//td[@class='label']//span[@class='txt']/text()").extract()[0::2]
        balanco_label += list(map(lambda label: label + "_ult._12_meses", dre_12_meses))
        dre_3_meses = self._get_html_selector().xpath(
            "//table[5]//td[@class='label w2']//span[@class='txt']/text() | "
            "//table[5]//td[@class='label']//span[@class='txt']/text()").extract()[1::2]
        balanco_label += list(map(lambda label: label + "_ult._3_meses", dre_3_meses))
        return balanco_label

    def extrair_dados_valores(self):
        balanco_dados = self._get_html_selector().xpath(
            "//table[2]//span[@class='txt']/text()").extract()[2:6][1::2]
        balanco_dados += self._get_html_selector().xpath(
            "//table[4]//td[@class='data w3']//span[@class='txt']/text() | "
            "//table[4]//td[@class='data']//span[@class='txt']/text()").extract()
        balanco_dados += self._get_html_selector().xpath(
            "//table[5]//td[@class='data w3']//span[@class='txt']/text() | "
            "//table[5]//td[@class='data']//span[@class='txt']/text()").extract()[0::2]
        balanco_dados += self._get_html_selector().xpath(
            "//table[5]//td[@class='data w3']//span[@class='txt']/text() | "
            "//table[5]//td[@class='data']//span[@class='txt']/text()").extract()[1::2]
        return balanco_dados
