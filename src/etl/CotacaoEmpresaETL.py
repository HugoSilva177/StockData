from src.etl.ProcessoETL import ProcessoETL
from src.dao.fundamentus.CotacaoEmpresaDAO import CotacaoEmpresaDAO
from src.web_scraping.fundamentus_web.CotacaoEmpresaScraping import CotacaoEmpresaScraping


class CotacaoEmpresaETL(ProcessoETL):

    def __init__(self, papel, id_empresa_inserida):
        super().__init__(CotacaoEmpresaScraping(papel), CotacaoEmpresaDAO())
        self.__id_empresa_inserida = id_empresa_inserida

    def iniciar_cotacao_etl(self):
        cotacao_empresa_label, cotacao_empresa_dados = self._extrair_dados_empresa()
        cotacao_empresa = self._transformar_dados_empresa(cotacao_empresa_label,
                                                          cotacao_empresa_dados)
        cotacao_empresa['Empresa'] = self.__id_empresa_inserida
        id_cotacao_inserido = self._gravar_dados_empresa_db(cotacao_empresa)
        return id_cotacao_inserido


"""
    def __extrair_dados_cotacao_empresa(self):
        extracao_dados = CotacaoEmpresaScraping(self.__papel)
        cotacao_empresa_label = extracao_dados.extrair_cotacao_empresa_dados()
        cotacao_empresa_dados = extracao_dados.extrair_cotacao_empresa_dados()
        return cotacao_empresa_label, cotacao_empresa_dados

    def __transformar_dados_cotacao_empresa(self, cotacao_empresa_label, cotacao_empresa_dados):
        transformacao_dados = DadosTransformacao()
        cotacao_empresa_label = transformacao_dados.remover_caracteres_especiais(cotacao_empresa_label)
        cotacao_empresa_label.insert(0, 'Papel')
        cotacao_empresa_dados.insert(0, self.__papel)
        cotacao_empresa = transformacao_dados.transformar_listas_em_dicionario(cotacao_empresa_label, cotacao_empresa_dados)
        return cotacao_empresa

    def __gravar_dados_cotacao_empresa_db(self, info_empresa):
        cotacao_dao = CotacaoEmpresaDAO()
        cotacao_dao.inserir_cotacao_empresa(info_empresa)
        id_inserido_cotacao = cotacao_dao.get_id_inserido_cotacao()
        return id_inserido_cotacao
"""
