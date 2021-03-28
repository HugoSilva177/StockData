from web_scraping.fundamentus.src.scraping.DataScraping import DataScraping


class EmpresaBusiness:

    def __init__(self, scraping_object):
        self.__scraping_object = scraping_object

    def iniciar_web_scraping(self):
        dados_label, dados_valores = self.__scraping_object.iniciar_web_scraping_label_valores()
        dados_label_valores = {"dados_label": dados_label, "dados_valores": dados_valores}
        return dados_label_valores


    @staticmethod
    def verificar_dados_empresa_exitem(papel, dao_object):
        dados_empresa = dao_object.buscar_dados_empresa(papel)
        if (dados_empresa is None) or (len(dados_empresa) == 0):
            return None
        else:
            return dados_empresa

    @staticmethod
    def verificar_ultima_cotacao_existe(papel, dao_object):
        data_ultima_cotacao_scraping = DataScraping(papel).extrair_data_ult_cotacao()
        print(f"Data última cotação Web Scraping: {data_ultima_cotacao_scraping}")
        ultima_cotacao = dao_object.buscar_dados_empresa(papel,
                                                         data_ultima_cotacao_scraping)
        print(f"Data última cotacação: {ultima_cotacao}")
        if (ultima_cotacao is None) or (len(ultima_cotacao) == 0):
            return True
        else:
            return False

    @staticmethod
    def verificar_ultimo_balanco_existe(papel, dao_object):
        data_ultimo_balanco = DataScraping(papel).extrair_data_ult_balanco()
        utlimo_balanco = dao_object.buscar_dados_empresa(papel, data_ultimo_balanco)
        print(f"Data último balanço: {data_ultimo_balanco}")
        if (utlimo_balanco is None) or (len(utlimo_balanco) == 0):
            return True
        else:
            return False

