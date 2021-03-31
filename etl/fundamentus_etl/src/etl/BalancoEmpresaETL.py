from etl.fundamentus_etl.src.etl import ProcessoETL
from etl.fundamentus_etl import BalancoEmpresaDAO
from etl.fundamentus_etl import BalancoEmpresaHDFS
from etl.fundamentus_etl import BalancoEmpresaScraping


class BalancoEmpresaETL(ProcessoETL):

    def __init__(self, papel, id_dados_empresa):
        super().__init__(BalancoEmpresaScraping(papel), BalancoEmpresaDAO(), BalancoEmpresaHDFS())
        self.__id_dados_empresa = id_dados_empresa
        self.__papel = papel

    def iniciar_balanco_empresa_etl(self):
        balanco_empresa_label, balanco_empresa_dados = self._extrair_dados_empresa(['Id_Empresa', 'Papel'],
                                                                                   [self.__id_dados_empresa,
                                                                                    self.__papel])
        dados_empresa_dicionario, dados_empresa_spark_df = self._transformar_dados_empresa(balanco_empresa_label,
                                                                                           balanco_empresa_dados)
        self._gravar_dados_empresa(dados_empresa_dicionario, dados_empresa_spark_df)
