from web_scraping.fundamentus.src.dao.hadoop_hdfs.InfoEmpresaHDFS import InfoEmpresaHDFS
from web_scraping.fundamentus.src.dao.hadoop_hdfs.CotacaoEmpresaHDFS import CotacaoEmpresaHDFS
from web_scraping.fundamentus.src.dao.hadoop_hdfs.BalancoEmpresaHDFS import BalancoEmpresaHDFS
from web_scraping.fundamentus.src.business.validacao_business.DadosValidacao import DadosValidacao


class DadosValidacaoHDFS(DadosValidacao):

    def __init__(self, papel, html_selector):
        super().__init__(papel, html_selector, InfoEmpresaHDFS(), CotacaoEmpresaHDFS(), BalancoEmpresaHDFS())
