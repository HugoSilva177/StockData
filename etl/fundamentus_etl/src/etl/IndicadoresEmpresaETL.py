from etl.fundamentus_etl.src.etl import ProcessoETL
from etl.fundamentus_etl import IndicadoresDAO
from etl.fundamentus_etl.src.dao.mongodb.CotacaoEmpresaDAO import CotacaoEmpresaDAO
from etl.fundamentus_etl import IndicadoresEmpresaHDFS
from etl.fundamentus_etl import IndicadoresEmpresaScraping


class IndicadoresEmpresaETL(ProcessoETL):

    def __init__(self, papel, id_inserido_cotacao):
        super().__init__(IndicadoresEmpresaScraping(papel), IndicadoresDAO(), IndicadoresEmpresaHDFS())
        self.__papel = papel
        self.__id_inserido_cotacao = id_inserido_cotacao


    def iniciar_indicadores_etl(self):
        indicadores_empresa_label, indicadores_empresa_dados = self._extrair_dados_empresa(['Id_Cotacao', 'Papel'],
                                                                                           [self.__id_inserido_cotacao,
                                                                                            self.__papel])
        dados_empresa_dicionario, dados_empresa_spark_df = self._transformar_dados_empresa(indicadores_empresa_label, indicadores_empresa_dados)
        indicadores_empresa = self._gravar_dados_empresa(dados_empresa_dicionario, dados_empresa_spark_df)
        self.__incluir_id_indicadores_na_colecao_cotacao(indicadores_empresa)

    def __incluir_id_indicadores_na_colecao_cotacao(self, id_indicadores):
        CotacaoEmpresaDAO().inserir_indicadores_na_cotacao(self.__id_inserido_cotacao,
                                                           id_indicadores)

