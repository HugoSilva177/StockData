from src.dao.fundamentus.AbstractMongoDAO import AbstractMongoDAO
from src.etl.DadosTransformacao import DadosTransformacao
from src.web_scraping.fundamentus_web.WebScraping import WebScraping


class ProcessoETL():

    def __init__(self, web_scraping_object, dao_object):
        self.__web_scraping_object = web_scraping_object
        self.__dao_object = dao_object

    def _extrair_dados_empresa(self, dados_label, dados_valores):
        dados_label += self.__web_scraping_object.extrair_dados_label()
        dados_valores += self.__web_scraping_object.extrair_dados_valores()
        return dados_label, dados_valores

    def _transformar_dados_empresa(self, dados_label, dados_valores):
        transformacao_dados = DadosTransformacao()
        dados_label = transformacao_dados.remover_caracteres_especiais(dados_label)
        dados_empresa_dicionario = transformacao_dados.transformar_listas_em_dicionario(dados_label,
                                                                                        dados_valores)
        return dados_empresa_dicionario

    def _gravar_dados_empresa_db(self, dados_empresa):
        id_dado_inserido = self.__dao_object.inserir_dados(dados_empresa)
        return id_dado_inserido






