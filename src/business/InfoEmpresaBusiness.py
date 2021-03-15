from src.business.DadosTransformacao import DadosTransformacao
from src.dao.fundamentus_dao.InfoEmpresaDAO import InfoEmpresaDAO
from src.web_scraping.fundamentus_web.InfoEmpresaScraping import InfoEmpresaScraping


class InfoEmpresaBusiness:

    def __init__(self, papel):
        self.__extracao_dados = InfoEmpresaScraping(papel)
        self.__transformacao_dados = DadosTransformacao()
        self.__conexao_db = InfoEmpresaDAO()


    def iniciar_web_scraping_etl(self):
        info_empresa_label, info_empresa_dados = self.__extrair_dados_info_empresa()
        info_empresa = self.__transformar_dados_info_empresa(info_empresa_label, info_empresa_dados)
        self.__adicionar_dados_info_empresa_db(info_empresa)

    def __extrair_dados_info_empresa(self):
        info_empresa_label = self.__extracao_dados.extrair_info_empresa_label()
        info_empresa_dados = self.__extracao_dados.extrair_info_empresa_dados()
        return info_empresa_label, info_empresa_dados

    def __transformar_dados_info_empresa(self, info_empresa_label, info_empresa_dados):
        info_empresa_label = self.__transformacao_dados.remover_caracteres_especiais(info_empresa_label)
        info_empresa = self.__transformacao_dados.transformar_listas_em_dicionario(info_empresa_label, info_empresa_dados)
        return info_empresa

    def __adicionar_dados_info_empresa_db(self, info_empresa):
        self.__conexao_db.inserir_dados_empresa(info_empresa)

