from scrapy import Selector
from abc import ABCMeta, abstractmethod
from urllib.request import Request, urlopen


class WebScraping(metaclass=ABCMeta):

    def __init__(self, papel):
        self.__papel = papel
        self.__erro = None

    @abstractmethod
    def extrair_dados_label(self):
        return

    @abstractmethod
    def extrair_dados_valores(self):
        return

    def _get_html_selector(self):
        url = 'https://fundamentus.com.br/detalhes.php?papel=%s' % self.__papel
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        response = urlopen(req, timeout=20).read()
        html_dados = response.decode('latin-1')

        html_selector = Selector(text=html_dados)
        conteudo_url_nao_existe = len(html_selector.xpath("//table"))
        if conteudo_url_nao_existe == 0:
            raise Exception('URL não é válida')
        return html_selector

    def get_erro(self):
        return self.__erro
