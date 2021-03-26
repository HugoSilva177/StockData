
class EmpresaBusiness:

    def __init__(self, scraping_object):
        self.__scraping_object = scraping_object

    def iniciar_web_scraping(self):
        dados_label, dados_valores = self.__scraping_object.iniciar_web_scraping_label_valores()
        dados_label_valores = {"dados_label": dados_label, "dados_valores": dados_valores}
        return dados_label_valores