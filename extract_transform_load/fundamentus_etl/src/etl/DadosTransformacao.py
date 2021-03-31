from datetime import datetime
from unicodedata import normalize


class DadosTransformacao:

    @staticmethod
    def remover_acentos(txt):
        return normalize('NFKD', txt).encode('ASCII', 'ignore').decode('ASCII')

    @staticmethod
    def remover_caracteres_especiais(empresa_label):
        empresa_label = list(map(lambda x: DadosTransformacao.remover_acentos(x), empresa_label))
        empresa_label = list(map(lambda st: str.replace(st, " ","_"), empresa_label))
        empresa_label = list(map(lambda st: str.replace(st, "(",""), empresa_label))
        empresa_label = list(map(lambda st: str.replace(st, ")",""), empresa_label))
        empresa_label = list(map(lambda st: str.replace(st, ".",""), empresa_label))
        return empresa_label

    @staticmethod
    def transformar_lista_em_tuples(empresa_dados):
        empresa_dados_list = []
        empresa_dados_list.append(tuple(empresa_dados))
        return empresa_dados_list

    @staticmethod
    def transformar_listas_em_dicionario(lista_keys, lista_values):
        novo_dicionario = {lista_keys[i]: lista_values[i] for i in range(len(lista_keys))}
        return novo_dicionario