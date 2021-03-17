from src.business.InfoEmpresaBusiness import InfoEmpresaBusiness
from src.business.CotacaoEmpresaBusiness import CotacaoEmpresaBusiness
from src.business.BalancoEmpresaBusiness import BalancoEmpresaBusiness

info_empresa_business = InfoEmpresaBusiness('PETR4')
id_empresa_inserida = info_empresa_business.iniciar_web_scraping()

cotacao_empresa_business = CotacaoEmpresaBusiness('PETR4', id_empresa_inserida)
cotacao_empresa_business.iniciar_web_scraping()

balanco_empresa = BalancoEmpresaBusiness('PETR4')
balanco_empresa.iniciar_web_scraping()