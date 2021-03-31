


class EmpresaBusiness:

    def __init__(self, dados_empresa):
        self.__dados_empresa = dados_empresa
        self.__id_cotacao = None

    def empresa_etl_business(self):

        for label_dados in self.__dados_empresa:
            dados_label = self.__dados_empresa[label_dados]['dados_label']
            dados_valores = self.__dados_empresa[label_dados]['dados_label']

            if label_dados == 'Info':
                pass
            elif label_dados == 'Cotacao':
                pass
            elif label_dados == 'Oscilacoes':
                pass
            elif label_dados == 'Indicadores':
                pass
            elif label_dados == 'Balanco':
                pass

    def iniciar_etl_info_empresa(self):
        pass
        # ETL DE INFO

    def iniciar_etl_cotacao_empresa(self):
        pass
        # ETL CCOTACAO

    def iniciar_etl_oscilacoes_empresa(self):
        pass
        # ETL OSCILACOES

    def iniciar_etl_indicadores_empresa(self):
        pass
        # ETL INDICADORES

    def iniciar_etl_balanco_empresa(self):
        pass
        # ETL BALANÇO













