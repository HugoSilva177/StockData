from src.business.DadosTransformacao import DadosTransformacao
from src.dao.fundamentus_dao.CotacaoEmpresaDAO import CotacaoEmpresaDAO
from src.web_scraping.fundamentus_web.CotacaoEmpresaScraping import CotacaoEmpresaScraping
from src.business.OscilacoesEmpresaBusiness import OscilacoesEmpresaBusiness

class CotacaoEmpresaETL:

    def __init__(self, papel):
        self.__papel = papel
        self.__extracao_dados = CotacaoEmpresaScraping(papel)
        self.__transformacao_dados = DadosTransformacao( )
        self.__cotacao_dao = CotacaoEmpresaDAO( )

    def extrair_dados_cotacao_empresa(self):
        cotacao_empresa_label = self.__extracao_dados.extrair_cotacao_empresa_dados()
        cotacao_empresa_dados = self.__extracao_dados.extrair_cotacao_empresa_dados()
        return cotacao_empresa_label, cotacao_empresa_dados

    def transformar_dados_cotacao_empresa(self, cotacao_empresa_label, cotacao_empresa_dados):
        cotacao_empresa_label = self.__transformacao_dados.remover_caracteres_especiais(cotacao_empresa_label)
        cotacao_empresa_label.insert(0, 'Papel')
        cotacao_empresa_dados.insert(0, self.__papel)
        cotacao_empresa = self.__transformacao_dados.transformar_listas_em_dicionario(cotacao_empresa_label, cotacao_empresa_dados)
        return cotacao_empresa

    def adicionar_dados_cotacao_empresa_db(self, info_empresa):
        self.__cotacao_dao.inserir_cotacao_empresa(info_empresa)