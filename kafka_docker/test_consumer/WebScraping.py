from kafka_docker.test_consumer.WebScrapingConsumer import WebScrapingConsumer
import json


class WebScraping:

    def __init__(self):
        self.__execucao_web_scraping_consumer = True
        self.__web_scraping_consumer = WebScrapingConsumer(['web_scraping_mongo'])

    def empresa_etl_web_scraping_business(self):
        while True:
            mensagem = self.__web_scraping_consumer.mensagem_dados_empresa_consumer()
            if mensagem is None:
                continue
            else:
                lista_dados_empresa = self.__processar_mensagem(mensagem)
                for dados_empresa_key in lista_dados_empresa:
                    dados_empresa = lista_dados_empresa[dados_empresa_key]
                    if dados_empresa_key == 'Info':
                        print(dados_empresa)
                    elif dados_empresa_key == 'Cotacao':
                        print(dados_empresa)
                    elif dados_empresa_key == 'Oscilacoes':
                        print(dados_empresa)
                    elif dados_empresa_key == 'Indicadores':
                        print(dados_empresa)
                    elif dados_empresa_key == 'Balanco':
                        print(dados_empresa)

    def __processar_mensagem(self, mensagem):
        dados_empresa = json.loads(mensagem.value().decode('utf-8'))
        return dados_empresa
