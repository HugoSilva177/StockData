from scrapy import Selector
from abc import ABCMeta, abstractmethod
from urllib.request import Request, urlopen


class WebScraping(metaclass=ABCMeta):

    def __init__(self, papel):
        self.__papel = papel
        self.__erro = None
        self.__html_selector = None
        url = 'https://fundamentus.com.br/detalhes.php?papel=%s' % self.__papel
        try:
            req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            response = urlopen(req, timeout=20).read()
            html_dados = response.decode('latin-1')

            self.__html_selector = Selector(text=html_dados)
        except Exception:
            self.__erro = 'Erro ao iniciar Web Scraping'

    @abstractmethod
    def extrair_dados_label(self):
        return

    @abstractmethod
    def extrair_dados_valores(self):
        return

    def get_html_selector(self):
        return self.__html_selector

    def get_erro(self):
        return self.__erro
