from scrapy import Selector
from urllib.request import Request, urlopen
from web_scraping.fundamentus.src.exceptions.PapelInvalidoError import PapelInvalidoError


class RequestHtmlSelector:

    def __init__(self):
        self.__html_selector = None

    @staticmethod
    def get_html_selector(papel):
        url = 'https://fundamentus.com.br/detalhes.php?papel=%s' % papel
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        response = urlopen(req, timeout=20).read()
        html_dados = response.decode('latin-1')

        html_selector = Selector(text=html_dados)
        conteudo_url_nao_existe = len(html_selector.xpath("//table[@class='w728']"))
        if conteudo_url_nao_existe == 0:
            raise PapelInvalidoError('Nome do papel não é válido!')
        return html_selector
