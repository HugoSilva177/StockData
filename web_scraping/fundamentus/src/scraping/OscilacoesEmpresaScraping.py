from web_scraping.fundamentus.src.scraping.WebScraping import WebScraping
from web_scraping.fundamentus.src.scraping.DataScraping import DataScraping


class OscilacoesEmpresaScraping(WebScraping):

    def __init__(self, papel, html_selector):
        super().__init__()
        self.__papel = papel
        self.__html_selector = html_selector

    def scraping_dados_label(self):
        oscilacao_label = self.__html_selector.xpath(
            "//table[3]//td[@class='nivel1']//span/text()").extract()[0]
        lista_oscilacoes_label = self.__html_selector.xpath(
            "//table[3]//td[@class='label w1']//span/text()").extract()
        oscilacoes_label = list(map(lambda label: oscilacao_label + "_" + label, lista_oscilacoes_label))
        oscilacoes_label.insert(0, 'Data_ult_cot')
        oscilacoes_label.insert(0, 'Papel')
        return oscilacoes_label

    def extrair_dados_valores(self):
        data_ult_cotacao = DataScraping(self.__html_selector).extrair_data_ult_cotacao()
        oscilacoes_dados = self.__html_selector.xpath(
            "//table[3]//span[@class='oscil']/font/text()").extract()
        oscilacoes_dados.insert(0, data_ult_cotacao)
        oscilacoes_dados.insert(0, self.__papel)
        return oscilacoes_dados
