import json
from extract_transform_load.fundamentus_etl.src.etl.InfoEmpresaETL import InfoEmpresaETL
from extract_transform_load.fundamentus_etl.src.etl.CotacaoEmpresaETL import CotacaoEmpresaETL
from extract_transform_load.fundamentus_etl.src.etl.BalancoEmpresaETL import BalancoEmpresaETL
from extract_transform_load.fundamentus_etl.src.etl.OscilacoesEmpresaETL import OscilacoesEmpresaETL
from extract_transform_load.fundamentus_etl.src.kafka.WebScrapingConsumer import WebScrapingConsumer
from extract_transform_load.fundamentus_etl.src.etl.IndicadoresEmpresaETL import IndicadoresEmpresaETL


class EmpresaBusiness:

    def __init__(self):
        self.__id_cotacao = None
        self.__execucao_web_scraping_consumer = True
        self.__web_scraping_consumer = WebScrapingConsumer(['web_scraping_mongo', 'web_scraping_hdfs'])
        self.__dados_empresa = None

    def empresa_etl_web_scraping_business(self):
        while self.__execucao_web_scraping_consumer:
            mensagem = self.__web_scraping_consumer.mensagem_dados_empresa_consumer()
            if mensagem is None:
                continue
            else:
                lista_dados_empresa = self.__processar_mensagem(mensagem)
                for label_dados in lista_dados_empresa:
                    self.__dados_empresa = lista_dados_empresa[label_dados]
                    if label_dados == 'Info':
                        self.__iniciar_etl_info_empresa()
                    elif label_dados == 'Cotacao':
                        self.__iniciar_etl_cotacao_empresa()
                    elif label_dados == 'Oscilacoes':
                        self.__iniciar_etl_oscilacoes_empresa()
                    elif label_dados == 'Indicadores':
                        self.__iniciar_etl_indicadores_empresa()
                    elif label_dados == 'Balanco':
                        self.__iniciar_etl_balanco_empresa()

    def __processar_mensagem(self, mensagem):
        dados_empresa = json.loads(mensagem.value().decode('utf-8'))
        return dados_empresa

    def __iniciar_etl_info_empresa(self):
        InfoEmpresaETL(self.__dados_empresa).info_empresa_etl()

    def __iniciar_etl_cotacao_empresa(self):
        CotacaoEmpresaETL(self.__dados_empresa).cotacao_empresa_etl()

    def __iniciar_etl_oscilacoes_empresa(self):
        OscilacoesEmpresaETL(self.__dados_empresa).oscilacoes_empresa_etl()

    def __iniciar_etl_indicadores_empresa(self):
        IndicadoresEmpresaETL(self.__dados_empresa).indicadores_empresa_etl()

    def __iniciar_etl_balanco_empresa(self):
        BalancoEmpresaETL(self.__dados_empresa).balanco_empresa_etl()













