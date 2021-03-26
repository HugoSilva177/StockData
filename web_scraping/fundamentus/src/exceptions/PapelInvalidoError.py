class PapelInvalidoError(Exception):

    def __init__(self, mensagem_erro):
        self.__mensagem_erro = mensagem_erro

    def get_mensagem_erro(self):
        return self.__mensagem_erro