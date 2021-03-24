from src.dao.fundamentus.AbstractMongoDAO import AbstractMongoDAO
from src.etl.DadosTransformacao import DadosTransformacao
from src.web_scraping.fundamentus_web.WebScraping import WebScraping
import pandas as pd
from pyspark.sql import SparkSession

class ProcessoETL:

    def __init__(self, web_scraping_object, dao_object):
        self.__web_scraping_object = web_scraping_object
        self.__dao_object = dao_object
        self.__transformacao_dados = DadosTransformacao()
        self.__spark_session = SparkSession.builder.appName("write-read-fundamentus-hdfs").getOrCreate()

    def _extrair_dados_empresa(self, dados_label, dados_valores):
        dados_label += self.__web_scraping_object.extrair_dados_label()
        dados_valores += self.__web_scraping_object.extrair_dados_valores()
        return dados_label, dados_valores

    def _transformar_dados_empresa(self, dados_label, dados_valores):
        dados_label = self.__transformacao_dados.remover_caracteres_especiais(dados_label)
        dados_empresa_dicionario = self.__transforma_dados_empresa_mongodb(dados_label, dados_valores)
        dados_empresa_spark_df = self.__transformar_dados_empresa_hdfs(dados_label, dados_valores)
        return dados_empresa_dicionario, dados_empresa_spark_df

    def __transforma_dados_empresa_mongodb(self, dados_label, dados_valores):
        dados_empresa_dicionario = self.__transformacao_dados.transformar_listas_em_dicionario(dados_label,
                                                                                               dados_valores)
        return dados_empresa_dicionario

    def __transformar_dados_empresa_hdfs(self, dados_label, dados_valores):
        dados_valores = self.__transformacao_dados.transformar_lista_em_tuples(dados_valores)
        dados_empresa_spark_df = self.__spark_session.createDataFrame(dados_label, dados_valores)
        return dados_empresa_spark_df

    def _gravar_dados_empresa(self, dados_empresa_dicionario, dados_empresa_spark_df):
        id_dado_inserido_mongodb = self.__gravar_dados_empresa_mongodb(dados_empresa_dicionario)
        self.__gravar_dados_empresa_hdfs(dados_empresa_spark_df)

    def __gravar_dados_empresa_mongodb(self, dados_empresa_dicionario):
        id_dado_inserido = self.__dao_object.inserir_dados(dados_empresa_dicionario)
        return id_dado_inserido

    def __gravar_dados_empresa_hdfs(self, dados_empresa_spark_df):
        pass






