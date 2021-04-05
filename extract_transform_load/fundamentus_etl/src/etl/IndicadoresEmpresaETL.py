from extract_transform_load.fundamentus_etl.src.etl.ProcessoETL import ProcessoETL
from extract_transform_load.fundamentus_etl.src.dao.mongodb.IndicadoresDAO import IndicadoresDAO
from extract_transform_load.fundamentus_etl.src.dao.mongodb.CotacaoEmpresaDAO import CotacaoEmpresaDAO
from extract_transform_load.fundamentus_etl.src.dao.hadoop_hdfs.IndicadoresEmpresaHDFS import IndicadoresEmpresaHDFS


class IndicadoresEmpresaETL(ProcessoETL):

    def __init__(self, dados_empresa, id_inserido_cotacao):
        super().__init__(IndicadoresDAO(), IndicadoresEmpresaHDFS())
        self.__dados_empresa = dados_empresa
        self.__id_inserido_cotacao = id_inserido_cotacao


    def indicadores_empresa_etl(self):
        indicadores_empresa_label, indicadores_empresa_dados = self._extrair_dados_empresa(self.__dados_empresa)

        dados_empresa_dicionario, dados_empresa_spark_df = self._transformar_dados_empresa(indicadores_empresa_label,
                                                                                           indicadores_empresa_dados)
        indicadores_empresa = self._gravar_dados_empresa(dados_empresa_dicionario, dados_empresa_spark_df)
        self.__incluir_id_indicadores_na_colecao_cotacao(indicadores_empresa)

    def __incluir_id_indicadores_na_colecao_cotacao(self, id_indicadores):
        CotacaoEmpresaDAO().inserir_indicadores_na_cotacao(self.__id_inserido_cotacao,
                                                           id_indicadores)

