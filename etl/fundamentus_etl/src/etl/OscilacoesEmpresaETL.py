from etl.fundamentus_etl.src.etl import ProcessoETL
from etl.fundamentus_etl.src.dao.mongodb.CotacaoEmpresaDAO import CotacaoEmpresaDAO
from etl.fundamentus_etl import OscilacoesEmpresaDAO
from etl.fundamentus_etl import OscilacoesEmpresaHDFS
from etl.fundamentus_etl import OscilacoesEmpresaScraping


class OscilacoesEmpresaETL(ProcessoETL):

    def __init__(self, papel, id_inserido_cotacao):
        super().__init__(OscilacoesEmpresaScraping(papel), OscilacoesEmpresaDAO(), OscilacoesEmpresaHDFS())
        self.__papel = papel
        self.__id_inserido_cotacao = id_inserido_cotacao


    def iniciar_oscilacoes_etl(self):
        oscilacoes_empresa_label, oscilacoes_empresa_dados = self._extrair_dados_empresa(['Id_Cotacao', 'Papel'],
                                                                                         [self.__id_inserido_cotacao,
                                                                                          self.__papel])
        dados_empresa_dicionario, dados_empresa_spark_df = self._transformar_dados_empresa(oscilacoes_empresa_label, oscilacoes_empresa_dados)
        id_oscilacoes = self._gravar_dados_empresa(dados_empresa_dicionario, dados_empresa_spark_df)
        self.__incluir_id_oscilacoes_na_colecao_cotacao(id_oscilacoes)

    def __incluir_id_oscilacoes_na_colecao_cotacao(self, id_oscilacoes):
        CotacaoEmpresaDAO().inserir_oscilacoes_na_cotacao(self.__id_inserido_cotacao,
                                                          id_oscilacoes)

