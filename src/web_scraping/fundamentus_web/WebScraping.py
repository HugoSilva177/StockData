from scrapy import Selector
from urllib.request import Request, urlopen
from src.web_scraping.fundamentus_web.TransformData import validar_data

def baixar_html_site_fundamentus(papel):
    print(f"Baixando dados em HTML do '{papel}' no site fundamentus...")
    print("--------------------------------------------")
    url = 'https://fundamentus.com.br/detalhes.php?papel=%s' % papel

    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

    response = urlopen(req, timeout=20).read( )
    html_dados = response.decode('latin-1')

    global html_selector
    html_selector = Selector(text = html_dados)

def extrair_data_ult_cotacao():
    data_ult_cotacao = html_selector.xpath("//table[1]//span[@class='txt']/text() | // table[1]//span[@class='txt']/a/text()").extract()[7]
    data_ult_cotacao = validar_data(data_ult_cotacao)
    return data_ult_cotacao

def extrair_data_ult_balanco():
    data_ult_balanco = html_selector.xpath("//table[2]//span[@class='txt']/text()").extract()[3]
    data_ult_balanco = validar_data(data_ult_balanco)
    return data_ult_balanco