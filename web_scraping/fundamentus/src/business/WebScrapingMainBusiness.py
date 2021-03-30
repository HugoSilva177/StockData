from web_scraping.fundamentus.src.exceptions.PapelInvalidoError import PapelInvalidoError
from web_scraping.fundamentus.src.business.validacao_business.DadosValidacaoMongo import DadosValidacaoMongo
from web_scraping.fundamentus.src.business.validacao_business.DadosValidacaoHDFS import DadosValidacaoHDFS
from web_scraping.fundamentus.src.kafka.WebScrapingProducer import WebScrapingProducer



class WebScrapingMainBusiness:

    def __init__(self):
        self.__papel = None

    def fundamentus_web_scraping(self):
        nome_papel_invalido = True
        while nome_papel_invalido:
            self.__papel = input("Digite o nome do papel: ").upper()
            try:
                dados_empresa_mongo = DadosValidacaoMongo(self.__papel).validacao_dados_empresa()
                if dados_empresa_mongo is not None:
                    self.__enviar_dados_web_scraping('web_scraping_mongo', dados_empresa_mongo)
                dados_empresa_hdfs = DadosValidacaoHDFS(self.__papel).validacao_dados_empresa()
                if dados_empresa_hdfs is not None:
                    self.__enviar_dados_web_scraping('web_scraping_hdfs', dados_empresa_hdfs)
                nome_papel_invalido = False
            except PapelInvalidoError as err:
                print(f'Erro: {err.get_mensagem_erro()}')
                print('Tente novamente...')

    def __enviar_dados_web_scraping(self, topic, dados_empresa):
        web_scraping_producer = WebScrapingProducer()
        web_scraping_producer.criar_mensagem_producer(topic, dados_empresa)











