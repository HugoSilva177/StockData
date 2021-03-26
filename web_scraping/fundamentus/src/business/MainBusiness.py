from web_scraping.fundamentus.src.exceptions.PapelInvalidoError import PapelInvalidoError
from web_scraping.fundamentus.src.business.InfoEmpresaBusiness import InfoEmpresaBusiness

from fundamentus_etl.src.business.CotacaoEmpresaBusiness import CotacaoEmpresaBusiness
from fundamentus_etl.src.business.BalancoEmpresaBusiness import BalancoEmpresaBusiness


class EmpresaBusiness:

    def __init__(self):
        self.__papel = None

    def validacao_fundamentus_web_scraping(self):
        nome_papel_invalido = True
        while nome_papel_invalido:
            self.__papel = input("Digite o nome do papel: ").upper()
            try:
                self.__validacao_dados_empresa_mongodb()
                nome_papel_invalido = False
            except PapelInvalidoError as err:
                print(f'Erro: {err.get_mensagem_erro()}')
                print('Tente novamente...')

    def __validacao_dados_empresa_mongodb(self):
        id_dados_empresa = InfoEmpresaBusiness.verificar_dados_empresa_exitem_mongodb(self.__papel)
        print('-------------------------------------')
        print(f"Verificando se dados da empresa '{self.__papel}' existe....")
        if id_dados_empresa is None:
            pass
            # FAZER WEB SCRAPING COMPLETO (INFO_EMPRESA, COTAÇÃO E BALANÇO)
            # ENVIAR DADOS PARA O PROCESSO DE ETL DO MONGODB
        else:
            self.__validacao_dados_cotacao(id_dados_empresa)

    def __validacao_dados_cotacao(self, id_dados_empresa):
        if CotacaoEmpresaBusiness.verificar_ultima_cotacao_existe(id_dados_empresa, self.__papel):
            print('-------------------------------------')
            print('Dados da empresa já existe!')
            # FAZER WEB SCRAPING DA COTAÇÃO
            # ENVIAR DADOS PARA O PROCESSO DE ETL MONGODB
            print('** Dados da cotação incluídos com sucesso!')
            if BalancoEmpresaBusiness.verificar_ultimo_balanco_existe(id_dados_empresa, self.__papel):
                # FAZER WEB SCRAPING DO BALANÇO
                # ENVIAR DADOS PARA O PROCESSO DE ETL MONGODB
                print('** Dados da balanço incluídos com sucesso!')
            else:
                print('Dados do balanço já estão atualizados!')
            print('-------------------------------------')
            print('Finalizando Web Scraping!!!!')
        else:
            self.__validacao_dados_balanco(id_dados_empresa)

    def __validacao_dados_balanco(self, id_dados_empresa):
        if BalancoEmpresaBusiness.verificar_ultimo_balanco_existe(id_dados_empresa, self.__papel):
            print('Dados da Empresa e Cotação já estão atualizados!')
            print('-------------------------------------')
            # FAZER WEB SCRAPING DO BALANÇO
            # ENVIAR DADOS PARA O PROCESSO DE ETL MONGODB
            print('** Dados da balanço incluídos com sucesso!')
        else:
            print('Todos os dados já estão atualizados!')
        print('-------------------------------------')
        print('Finalizando Web Scraping!!!!')








