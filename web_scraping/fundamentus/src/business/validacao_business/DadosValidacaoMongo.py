from web_scraping.fundamentus.src.business.empresa_business.InfoEmpresaBusiness import InfoEmpresaBusiness
from web_scraping.fundamentus.src.business.empresa_business.WebScrapingBusiness import WebScrapingBusiness
from web_scraping.fundamentus.src.business.empresa_business.CotacaoEmpresaBusiness import CotacaoEmpresaBusiness
from web_scraping.fundamentus.src.business.empresa_business.BalancoEmpresaBusiness import BalancoEmpresaBusiness


class DadosValidacaoMongo:

    def __init__(self, papel):
        self.__papel = papel
        self.__web_scraping = WebScrapingBusiness(self.__papel)

    def validacao_dados_empresa_mongodb(self):
        id_dados_empresa = InfoEmpresaBusiness.verificar_dados_empresa_exitem_mongodb(self.__papel)
        print('-------------------------------------')
        print(f"Verificando se dados da empresa '{self.__papel}' existe....")
        if id_dados_empresa is None:
            self.__web_scraping.dados_empresa_web_scraping()
            # FAZER WEB SCRAPING COMPLETO (INFO_EMPRESA, COTAÇÃO E BALANÇO)
            # ENVIAR DADOS PARA O PROCESSO DE ETL DO MONGODB
        else:
            self.__validacao_dados_cotacao_mongodb()

    def __validacao_dados_cotacao_mongodb(self):
        if CotacaoEmpresaBusiness.verificar_ultima_cotacao_existe_mongodb(self.__papel):
            print('-------------------------------------')
            print('Dados da empresa já existe!')
            self.__web_scraping.cotacao_empresa_web_scraping()
            # FAZER WEB SCRAPING DA COTAÇÃO
            # ENVIAR DADOS PARA O PROCESSO DE ETL MONGODB
            print('** Dados da cotação incluídos com sucesso!')
            if BalancoEmpresaBusiness.verificar_ultimo_balanco_existe_mongodb(self.__papel):
                self.__web_scraping.balanco_empresa_web_scraping()
                # FAZER WEB SCRAPING DO BALANÇO
                # ENVIAR DADOS PARA O PROCESSO DE ETL MONGODB
                print('** Dados da balanço incluídos com sucesso!')
            else:
                print('Dados do balanço já estão atualizados!')
            print('-------------------------------------')
            print('Finalizando Web Scraping!!!!')
        else:
            self.__validacao_dados_balanco_mongodo()

    def __validacao_dados_balanco_mongodo(self):
        if BalancoEmpresaBusiness.verificar_ultimo_balanco_existe_mongodb(self.__papel):
            print('Dados da Empresa e Cotação já estão atualizados!')
            print('-------------------------------------')
            self.__web_scraping.balanco_empresa_web_scraping()
            # FAZER WEB SCRAPING DO BALANÇO
            # ENVIAR DADOS PARA O PROCESSO DE ETL MONGODB
            print('** Dados da balanço incluídos com sucesso!')
        else:
            print('Todos os dados já estão atualizados!')
        print('-------------------------------------')
        print('Finalizando Web Scraping!!!!')