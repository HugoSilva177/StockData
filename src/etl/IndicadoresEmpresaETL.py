from src.etl.ProcessoETL import ProcessoETL
from src.web_scraping.fundamentus_web.IndicadoresEmpresaScraping import IndicadoresEmpresaScraping
from src.dao.fundamentus.IndicadoresDAO import IndicadoresDAO

class IndicadoresEmpresaETL(ProcessoETL):

    def __init__(self, papel, id_inserido_cotacao):
        super().__init__(IndicadoresEmpresaScraping(papel), IndicadoresDAO(id_inserido_cotacao))
        self.__papel = papel
        self.__id_inserido_cotacao = id_inserido_cotacao


    def iniciar_indicadores_etl(self):
        indicadores_empresa_label, indicadores_empresa_dados = self._extrair_dados_empresa(['Id_Cotacao', 'Papel'],
                                                                                           [self.__id_inserido_cotacao,
                                                                                            self.__papel])
        indicadores_empresa = self._transformar_dados_empresa(indicadores_empresa_label, indicadores_empresa_dados)
        self._gravar_dados_empresa_db(indicadores_empresa)

