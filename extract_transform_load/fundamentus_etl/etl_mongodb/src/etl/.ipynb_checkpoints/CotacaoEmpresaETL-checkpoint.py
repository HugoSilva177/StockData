from extract_transform_load.fundamentus_etl.etl_mongodb.src.etl.ProcessoETL import ProcessoETL
from extract_transform_load.fundamentus_etl.etl_mongodb.src.dao.CotacaoEmpresaDAO import CotacaoEmpresaDAO


class CotacaoEmpresaETL(ProcessoETL):

    def __init__(self, dados_empresa):
        super().__init__(CotacaoEmpresaDAO())
        self.__dados_empresa = dados_empresa


    def cotacao_empresa_etl(self):
        cotacao_empresa_label, cotacao_empresa_dados = self._extrair_dados_empresa(self.__dados_empresa)
        dados_empresa_dicionario = self._transformar_dados_empresa(cotacao_empresa_label,
                                                                   cotacao_empresa_dados)
        id_cotacao_inserido = self._gravar_dados_empresa(dados_empresa_dicionario)
        return id_cotacao_inserido



