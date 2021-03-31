from web_scraping.fundamentus.src.business.empresa_business.EmpresaBusiness import EmpresaBusiness
from web_scraping.fundamentus.src.business.empresa_business.WebScrapingBusiness import WebScrapingBusiness


class DadosValidacao:

    def __init__(self, papel, html_selector, info_empresa_dao, cotacao_empresa_dao, balanco_empresa_dao):
        self.__html_selector = html_selector
        self.__web_scraping = WebScrapingBusiness(papel, html_selector)
        self.__papel = papel
        self.__info_empresa_dao = info_empresa_dao
        self.__cotacao_empresa_dao = cotacao_empresa_dao
        self.__balaco_empresa_dao = balanco_empresa_dao

    def validacao_dados_empresa(self):
        id_dados_empresa = EmpresaBusiness.verificar_dados_empresa_exitem(self.__papel,
                                                                          self.__info_empresa_dao)
        print('-------------------------------------')
        print(f"Verificando se dados da empresa '{self.__papel}' existe....")
        if id_dados_empresa is None:
            self.__web_scraping.dados_empresa_web_scraping()
            # FAZER WEB SCRAPING COMPLETO (INFO_EMPRESA, COTAÇÃO E BALANÇO)
            # ENVIAR DADOS PARA O PROCESSO DE ETL DO MONGODB
            print('-------------------------------------')
            print('Finalizando Web Scraping!!!!')
        else:
            self.__validacao_dados_cotacao()
            print('-------------------------------------')
            print('Finalizando Web Scraping!!!!')
        dados_empresa = self.__web_scraping.get_dados_empresa_label_valores()
        if len(dados_empresa) > 0:
            return dados_empresa
        else:
            return None

    def __validacao_dados_cotacao(self):
        if EmpresaBusiness.verificar_ultima_cotacao_existe(self.__papel,
                                                           self.__cotacao_empresa_dao,
                                                           self.__html_selector):
            print('Dados da empresa já existe!')
            print('-------------------------------------')
            self.__web_scraping.cotacao_empresa_web_scraping()
            # FAZER WEB SCRAPING DA COTAÇÃO
            # ENVIAR DADOS PARA O PROCESSO DE ETL MONGODB
            print('** Dados da cotação incluídos com sucesso!')
            if EmpresaBusiness.verificar_ultimo_balanco_existe(self.__papel,
                                                               self.__balaco_empresa_dao,
                                                               self.__html_selector):
                self.__web_scraping.balanco_empresa_web_scraping()
                # FAZER WEB SCRAPING DO BALANÇO
                # ENVIAR DADOS PARA O PROCESSO DE ETL MONGODB
                print('** Dados da balanço incluídos com sucesso!')
            else:
                print('Dados do balanço já estão atualizados!')
        else:
            self.__validacao_dados_balanco()

    def __validacao_dados_balanco(self):
        if EmpresaBusiness.verificar_ultimo_balanco_existe(self.__papel,
                                                           self.__balaco_empresa_dao,
                                                           self.__html_selector):
            print('Dados da Empresa e Cotação já estão atualizados!')
            print('-------------------------------------')
            self.__web_scraping.balanco_empresa_web_scraping()
            # FAZER WEB SCRAPING DO BALANÇO
            # ENVIAR DADOS PARA O PROCESSO DE ETL MONGODB
            print('** Dados da balanço incluídos com sucesso!')
        else:
            print('Todos os dados já estão atualizados!')
