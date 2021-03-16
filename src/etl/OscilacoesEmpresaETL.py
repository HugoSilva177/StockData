from src.business.DadosTransformacao import DadosTransformacao
from src.dao.fundamentus_dao.OscilacoesEmpresaDAO import OscilacoesEmpresaDAO
from src.web_scraping.fundamentus_web.OscilacoesEmpresaScraping import OscilacoesEmpresaScraping


class OscilacoesEmpresaETL:

    def __init__(self, papel):
        self.__papel = papel
        self.__extracao_dados = OscilacoesEmpresaScraping(papel)
        self.__transformacao_dados = DadosTransformacao()
        self.__conexao_db = OscilacoesEmpresaDAO()

    def extrair_dados_oscilacoes_empresa(self):
        oscilacoes_empresa_label = self.__extracao_dados.extrair_oscilacoes_empresa_label()
        oscilacoes_empresa_dados = self.__extracao_dados.extrair_oscilacoes_empresa_dados()
        return oscilacoes_empresa_label, oscilacoes_empresa_dados

    def transformar_dados_oscilacoes_empresa(self, oscilacoes_empresa_label, oscilacoes_empresa_dados):
        oscilacoes_empresa_label = self.__transformacao_dados.remover_caracteres_especiais(oscilacoes_empresa_label)
        oscilacoes_empresa_label.insert(0, 'Papel')
        oscilacoes_empresa_dados.insert(0, self.__papel)
        oscilacoes_empresa = self.__transformacao_dados.transformar_listas_em_dicionario(oscilacoes_empresa_label, oscilacoes_empresa_dados)
        return oscilacoes_empresa

    def adicionar_dados_oscilacoes_empresa_db(self, oscilacoes_empresa):
        self.__conexao_db.inserir_oscilacoes_empresa_mongodb(oscilacoes_empresa)