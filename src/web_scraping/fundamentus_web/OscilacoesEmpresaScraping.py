from src.web_scraping.fundamentus_web.WebScraping import WebScraping


class OscilacoesEmpresaScraping(WebScraping):

    def __init__(self, papel):
        super().__init__(papel)

    def extrair_oscilacoes_empresa_label(self):
        oscilacao_label = self.get_html_selector().xpath("//table[3]//td[@class='nivel1']//span/text()").extract( )[0]
        lista_oscilacoes_label = self.get_html_selector().xpath("//table[3]//td[@class='label w1']//span/text()").extract( )
        oscilacoes_label = list(map(lambda label: oscilacao_label + "_" + label, lista_oscilacoes_label))
        oscilacoes_label = remover_caracteres_especiais(oscilacoes_label)
        oscilacoes_label.insert(0, 'Papel')
        return oscilacoes_label

    def extrair_oscilacoes_empresa_dados(self):
        oscilacoes_dados = self.get_html_selector().xpath("//table[3]//span[@class='oscil']/font/text()").extract( )
        oscilacoes_dados.insert(0, papel)
        oscilacoes_dados = formatar_tipagem_dados(oscilacoes_dados)

        return oscilacoes_dados
