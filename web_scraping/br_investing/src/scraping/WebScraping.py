from abc import ABCMeta, abstractmethod


class WebScraping(metaclass=ABCMeta):

    def __init__(self):
        self.__erro = None

    def iniciar_web_scraping_noticias(self):
        pass

    @abstractmethod
    def scraping_dados_label(self):
        return

    @abstractmethod
    def scraping_dados_valores(self):
        return

    def get_erro(self):
        return self.__erro