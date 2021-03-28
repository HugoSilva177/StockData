from web_scraping.fundamentus.src.exceptions.PapelInvalidoError import PapelInvalidoError
from web_scraping.fundamentus.src.business.validacao_business.DadosValidacaoMongo import DadosValidacaoMongo
from web_scraping.fundamentus.src.business.validacao_business.DadosValidacaoHDFS import DadosValidacaoHDFS



class WebScrapingMainBusiness:

    def __init__(self):
        self.__papel = None

    def fundamentus_web_scraping(self):
        nome_papel_invalido = True
        while nome_papel_invalido:
            self.__papel = input("Digite o nome do papel: ").upper()
            try:
                DadosValidacaoMongo(self.__papel).validacao_dados_empresa()
                DadosValidacaoHDFS(self.__papel).validacao_dados_empresa()
                nome_papel_invalido = False
            except PapelInvalidoError as err:
                print(f'Erro: {err.get_mensagem_erro()}')
                print('Tente novamente...')










