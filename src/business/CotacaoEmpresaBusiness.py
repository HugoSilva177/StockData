from src.business.DadosTransformacao import DadosTransformacao
from src.dao.fundamentus_dao.CotacaoEmpresaDAO import CotacaoEmpresaDAO
from src.web_scraping.fundamentus_web.CotacaoEmpresaScraping import CotacaoEmpresaScraping


class CotacaoEmpresaBusiness:

    def __init__(self, papel):
        self.__papel = papel
        self.__extracao_dados = CotacaoEmpresaScraping(papel)
        self.__transformacao_dados = DadosTransformacao()
        self.__conexao_db = CotacaoEmpresaDAO()


    def iniciar_web_scraping_etl(self):
        cotacao_empresa_label, cotacao_empresa_dados = self.__extrair_dados_cotacao_empresa()
        cotacao_empresa = self.__transformar_dados_cotacao_empresa(cotacao_empresa_label, cotacao_empresa_dados)
        self.__adicionar_dados_cotacao_empresa_db(cotacao_empresa)

    def __extrair_dados_cotacao_empresa(self):
        cotacao_empresa_label = self.__extracao_dados.extrair_cotacao_empresa_dados()
        cotacao_empresa_dados = self.__extracao_dados.extrair_cotacao_empresa_dados()
        return cotacao_empresa_label, cotacao_empresa_dados

    def __transformar_dados_cotacao_empresa(self, cotacao_empresa_label, cotacao_empresa_dados):
        cotacao_empresa_label = self.__transformacao_dados.remover_caracteres_especiais(cotacao_empresa_label)
        cotacao_empresa_label.insert(0, 'Papel')
        cotacao_empresa_dados.insert(0, self.__papel)
        cotacao_empresa = self.__transformacao_dados.transformar_listas_em_dicionario(cotacao_empresa_label, cotacao_empresa_dados)
        return cotacao_empresa

    def __adicionar_dados_cotacao_empresa_db(self, info_empresa):
        self.__conexao_db.inserir_cotacao_empresa(info_empresa)


