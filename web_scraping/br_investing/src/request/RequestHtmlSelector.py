from scrapy import Selector
from urllib.request import Request, urlopen
from web_scraping.fundamentus.src.exceptions.PapelInvalidoError import PapelInvalidoError


class RequestHtmlSelector:

    @staticmethod
    def get_html_selector(papel):
        url_papel = 'petrobras-pn-news'
        url_completa_noticias = 'https://br.investing.com/equities/' + url_papel

        req = Request(url_completa_noticias, headers={'User-Agent': 'Mozilla/5.0'})

        response = urlopen(req, timeout=20).read()
        novas_noticias_html = response.decode('latin-1')
        # novas_noticias_html= response.decode('utf8')

        html_selector = Selector(text=novas_noticias_html)
        noticias_nao_existem = len(html_selector.xpath("//div[@class='mediumTitle1']/article"))
        if noticias_nao_existem == 0:
            return None
        else:
            return html_selector
