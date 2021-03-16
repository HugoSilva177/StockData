from src.business.InfoEmpresaBusiness import InfoEmpresaBusiness
from src.business.CotacaoEmpresaBusiness import CotacaoEmpresaBusiness

info_empresa_business = InfoEmpresaBusiness('PETR4')
id_empresa_inserida = info_empresa_business.iniciar_web_scraping()

cotacao_empresa_business = CotacaoEmpresaBusiness('PETR4', id_empresa_inserida)
cotacao_empresa_business.iniciar_web_scraping()