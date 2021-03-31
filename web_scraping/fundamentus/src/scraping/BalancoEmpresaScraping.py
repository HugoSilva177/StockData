from web_scraping.fundamentus.src.scraping.WebScraping import WebScraping


class BalancoEmpresaScraping(WebScraping):

    def __init__(self, papel, html_selector):
        super().__init__()
        self.__html_selector = html_selector
        self.__papel = papel

    def scraping_dados_label(self):
        balanco_label = self.__html_selector.xpath(
            "//table[2]//span[@class='txt']/text()").extract()[2:6][0::2]
        balanco_label += self.__html_selector.xpath(
            "//table[4]//td[@class='label w2']//span[@class='txt']/text() | "
            "//table[4]//td[@class='label']//span[@class='txt']/text()").extract()
        dre_12_meses = self.__html_selector.xpath(
            "//table[5]//td[@class='label w2']//span[@class='txt']/text() | "
            "//table[5]//td[@class='label']//span[@class='txt']/text()").extract()[0::2]
        balanco_label += list(map(lambda label: label + "_ult._12_meses", dre_12_meses))
        dre_3_meses = self.__html_selector.xpath(
            "//table[5]//td[@class='label w2']//span[@class='txt']/text() | "
            "//table[5]//td[@class='label']//span[@class='txt']/text()").extract()[1::2]
        balanco_label += list(map(lambda label: label + "_ult._3_meses", dre_3_meses))
        balanco_label.insert(0, 'Papel')
        return balanco_label

    def extrair_dados_valores(self):
        balanco_dados = self.__html_selector.xpath(
            "//table[2]//span[@class='txt']/text()").extract()[2:6][1::2]
        balanco_dados += self.__html_selector.xpath(
            "//table[4]//td[@class='data w3']//span[@class='txt']/text() | "
            "//table[4]//td[@class='data']//span[@class='txt']/text()").extract()
        balanco_dados += self.__html_selector.xpath(
            "//table[5]//td[@class='data w3']//span[@class='txt']/text() | "
            "//table[5]//td[@class='data']//span[@class='txt']/text()").extract()[0::2]
        balanco_dados += self.__html_selector.xpath(
            "//table[5]//td[@class='data w3']//span[@class='txt']/text() | "
            "//table[5]//td[@class='data']//span[@class='txt']/text()").extract()[1::2]
        balanco_dados.insert(0, self.__papel)
        return balanco_dados
