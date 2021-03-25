from fundamentus_etl.src.business.InfoEmpresaBusiness import InfoEmpresaBusiness
from fundamentus_etl.src.exceptions.PapelInvalidoError import PapelInvalidoError
from fundamentus_etl.src.business.CotacaoEmpresaBusiness import CotacaoEmpresaBusiness
from fundamentus_etl.src.business.BalancoEmpresaBusiness import BalancoEmpresaBusiness


class EmpresaBusiness:

    def __init__(self):
        self.__papel = None

    def fundamentus_web_scraping(self):
        nome_papel_invalido = True
        while nome_papel_invalido:
            self.__papel = input("Digite o nome do papel: ").upper()
            try:
                self.__validacao_dados_empresa()
                nome_papel_invalido = False
            except PapelInvalidoError as err:
                print(f'Erro: {err.get_mensagem_erro()}')
                print('Tente novamente...')

    def __validacao_dados_empresa(self):
        id_dados_empresa = InfoEmpresaBusiness.verificar_dados_empresa_exitem(self.__papel)
        print('-------------------------------------')
        print(f"Verificando se dados da empresa '{self.__papel}' existe....")
        if id_dados_empresa is None:
            id_dados_empresa = InfoEmpresaBusiness(self.__papel).iniciar_web_scraping()
            CotacaoEmpresaBusiness(self.__papel).iniciar_web_scraping(id_dados_empresa)
            BalancoEmpresaBusiness(self.__papel).iniciar_web_scraping(id_dados_empresa)
            print('Todos os dados foram incluídos com sucesso!')
            print('-------------------------------------')
            print('Finalizando Web Scraping!!!!')
        else:
            self.__validacao_dados_cotacao(id_dados_empresa)

    def __validacao_dados_cotacao(self, id_dados_empresa):
        if CotacaoEmpresaBusiness.verificar_ultima_cotacao_existe(id_dados_empresa, self.__papel):
            print('-------------------------------------')
            print('Dados da empresa já existe!')
            CotacaoEmpresaBusiness(self.__papel).iniciar_web_scraping(id_dados_empresa)
            print('** Dados da cotação incluídos com sucesso!')
            if BalancoEmpresaBusiness.verificar_ultimo_balanco_existe(id_dados_empresa, self.__papel):
                BalancoEmpresaBusiness(self.__papel).iniciar_web_scraping(id_dados_empresa)
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
            BalancoEmpresaBusiness(self.__papel).iniciar_web_scraping(id_dados_empresa)
            print('** Dados da balanço incluídos com sucesso!')
        else:
            print('Todos os dados já estão atualizados!')
        print('-------------------------------------')
        print('Finalizando Web Scraping!!!!')








