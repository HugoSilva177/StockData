from extract_transform_load.fundamentus_etl.etl_mongodb.src.etl.ProcessoETL import ProcessoETL
from extract_transform_load.fundamentus_etl.etl_mongodb.src.dao.CotacaoEmpresaDAO import CotacaoEmpresaDAO
from extract_transform_load.fundamentus_etl.etl_mongodb.src.dao.OscilacoesEmpresaDAO import OscilacoesEmpresaDAO


class OscilacoesEmpresaETL(ProcessoETL):

    def __init__(self, dados_empresa, id_inserido_cotacao):
        super().__init__(OscilacoesEmpresaDAO())
        self.__id_inserido_cotacao = id_inserido_cotacao
        self.__dados_empresa = dados_empresa

    def oscilacoes_empresa_etl(self):
        oscilacoes_empresa_label, oscilacoes_empresa_dados = self._extrair_dados_empresa(self.__dados_empresa)

        dados_empresa_dicionario = self._transformar_dados_empresa(oscilacoes_empresa_label,
                                                                   oscilacoes_empresa_dados)
        id_oscilacoes = self._gravar_dados_empresa(dados_empresa_dicionario)
        self.__incluir_id_oscilacoes_na_colecao_cotacao(id_oscilacoes)

    def __incluir_id_oscilacoes_na_colecao_cotacao(self, id_oscilacoes):
        CotacaoEmpresaDAO().inserir_oscilacoes_na_cotacao(self.__id_inserido_cotacao,
                                                          id_oscilacoes)


