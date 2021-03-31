from etl.fundamentus_etl.src.etl import ProcessoETL
from etl.fundamentus_etl.src.dao.mongodb.CotacaoEmpresaDAO import CotacaoEmpresaDAO
from etl.fundamentus_etl import CotacaoEmpresaHDFS
from etl.fundamentus_etl import CotacaoEmpresaScraping


class CotacaoEmpresaETL(ProcessoETL):

    def __init__(self, papel, id_empresa_inserida):
        super().__init__(CotacaoEmpresaScraping(papel), CotacaoEmpresaDAO(), CotacaoEmpresaHDFS())
        self.__id_empresa_inserida = id_empresa_inserida
        self.__papel = papel

    def iniciar_cotacao_etl(self):
        cotacao_empresa_label, cotacao_empresa_dados = self._extrair_dados_empresa(['Id_Empresa', 'Papel'],
                                                                                   [self.__id_empresa_inserida,
                                                                                    self.__papel])
        dados_empresa_dicionario, dados_empresa_spark_df = self._transformar_dados_empresa(cotacao_empresa_label,
                                                                                           cotacao_empresa_dados)
        id_cotacao_inserido = self._gravar_dados_empresa(dados_empresa_dicionario, dados_empresa_spark_df)
        return id_cotacao_inserido



