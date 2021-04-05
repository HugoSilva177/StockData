import json
from extract_transform_load.fundamentus_etl.src.etl.InfoEmpresaETL import InfoEmpresaETL
from extract_transform_load.fundamentus_etl.src.etl.CotacaoEmpresaETL import CotacaoEmpresaETL
from extract_transform_load.fundamentus_etl.src.etl.BalancoEmpresaETL import BalancoEmpresaETL
from extract_transform_load.fundamentus_etl.src.etl.OscilacoesEmpresaETL import OscilacoesEmpresaETL
from extract_transform_load.fundamentus_etl.src.kafka.WebScrapingConsumer import WebScrapingConsumer
from extract_transform_load.fundamentus_etl.src.etl.IndicadoresEmpresaETL import IndicadoresEmpresaETL


class EmpresaBusiness:

    def __init__(self):
        self.__execucao_web_scraping_consumer = True
        self.__web_scraping_consumer = WebScrapingConsumer(['web_scraping_mongo', 'web_scraping_hdfs'])
        self.__dados_empresa = None
        self.__id_inserido_cotacao = None

    def empresa_etl_web_scraping_business(self):
        while self.__execucao_web_scraping_consumer:
            mensagem = self.__web_scraping_consumer.mensagem_dados_empresa_consumer()
            if mensagem is None:
                continue
            else:
                lista_dados_empresa = self.__processar_mensagem(mensagem)
                for dados_empresa_key in lista_dados_empresa:
                    self.__dados_empresa = lista_dados_empresa[dados_empresa_key]
                    if dados_empresa_key == 'Info':
                        self.__iniciar_etl_info_empresa()
                    elif dados_empresa_key == 'Cotacao':
                        self.__iniciar_etl_cotacao_empresa()
                    elif dados_empresa_key == 'Oscilacoes':
                        self.__iniciar_etl_oscilacoes_empresa()
                    elif dados_empresa_key == 'Indicadores':
                        self.__iniciar_etl_indicadores_empresa()
                    elif dados_empresa_key == 'Balanco':
                        self.__iniciar_etl_balanco_empresa()

    def __processar_mensagem(self, mensagem):
        dados_empresa = json.loads(mensagem.value().decode('utf-8'))
        return dados_empresa

    def __iniciar_etl_info_empresa(self):
        InfoEmpresaETL(self.__dados_empresa).info_empresa_etl()

    def __iniciar_etl_cotacao_empresa(self):
        self.__id_inserido_cotacao = CotacaoEmpresaETL(self.__dados_empresa).cotacao_empresa_etl()

    def __iniciar_etl_oscilacoes_empresa(self):
        OscilacoesEmpresaETL(self.__dados_empresa, self.__id_inserido_cotacao).oscilacoes_empresa_etl()

    def __iniciar_etl_indicadores_empresa(self):
        IndicadoresEmpresaETL(self.__dados_empresa, self.__id_inserido_cotacao).indicadores_empresa_etl()

    def __iniciar_etl_balanco_empresa(self):
        BalancoEmpresaETL(self.__dados_empresa).balanco_empresa_etl()













