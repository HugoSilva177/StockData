from extract_transform_load.fundamentus_etl.etl_mongodb.src.etl.DadosTransformacao import DadosTransformacao


class ProcessoETL:

    def __init__(self, dao_object):
        self.__dao_object = dao_object

    def _extrair_dados_empresa(self, dados_empresa):
        dados_label = dados_empresa['dados_label']
        dados_valores = dados_empresa['dados_valores']
        return dados_label, dados_valores

    def _transformar_dados_empresa(self, dados_label, dados_valores):
        dados_label = DadosTransformacao.remover_caracteres_especiais(dados_label)
        dados_empresa_dicionario = DadosTransformacao.transformar_listas_em_dicionario(dados_label,
                                                                                       dados_valores)
        return dados_empresa_dicionario

    def _gravar_dados_empresa(self, dados_empresa_dicionario):
        id_dado_inserido = self.__dao_object.inserir_dados(dados_empresa_dicionario)
        return id_dado_inserido








