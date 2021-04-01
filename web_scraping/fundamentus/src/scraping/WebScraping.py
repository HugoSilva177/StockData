from scrapy import Selector
from abc import ABCMeta, abstractmethod
from urllib.request import Request, urlopen
from web_scraping.fundamentus.src.exceptions.PapelInvalidoError import PapelInvalidoError

class WebScraping(metaclass=ABCMeta):

    def __init__(self):
        self.__erro = None

    def iniciar_web_scraping_label_valores(self):
        dados_label = self.scraping_dados_label()
        dados_valores = self.scraping_dados_valores()

        return dados_label, dados_valores

    @abstractmethod
    def scraping_dados_label(self):
        return

    @abstractmethod
    def scraping_dados_valores(self):
        return

    def get_erro(self):
        return self.__erro
