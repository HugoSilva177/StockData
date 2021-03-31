from web_scraping.fundamentus.src.dao.mongo_db.InfoEmpresaDAO import InfoEmpresaDAO
from web_scraping.fundamentus.src.dao.mongo_db.CotacaoEmpresaDAO import CotacaoEmpresaDAO
from web_scraping.fundamentus.src.dao.mongo_db.BalancoEmpresaDAO import BalancoEmpresaDAO
from web_scraping.fundamentus.src.business.validacao_business.DadosValidacao import DadosValidacao


class DadosValidacaoMongo(DadosValidacao):

    def __init__(self, papel, html_selector):
        super().__init__(papel, html_selector, InfoEmpresaDAO(), CotacaoEmpresaDAO(), BalancoEmpresaDAO())
