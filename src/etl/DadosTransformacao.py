from datetime import datetime
from unicodedata import normalize


class DadosTransformacao:

    def remover_acentos(self, txt):
        return normalize('NFKD', txt).encode('ASCII', 'ignore').decode('ASCII')

    def remover_caracteres_especiais(self, empresa_label):
        empresa_label = list(map(lambda x: self.remover_acentos(x), empresa_label))
        empresa_label = list(map(lambda st: str.replace(st, " ","_"), empresa_label))
        empresa_label = list(map(lambda st: str.replace(st, "(",""), empresa_label))
        empresa_label = list(map(lambda st: str.replace(st, ")",""), empresa_label))
        empresa_label = list(map(lambda st: str.replace(st, ".",""), empresa_label))
        return empresa_label

    def validar_data(self, valor):
        try:
            valor = datetime.strptime(valor, '%d/%m/%Y')
            return valor
        except TypeError:
            return valor

    def formatar_tipagem_dados(self, empresa_dados):
        empresa_dados = list(map(lambda st: str.replace(st, ",", "."), empresa_dados))
        nova_lista_empresa_dados = []
        for valor in empresa_dados:
            eh_valor_percentual = valor.endswith('%')
            if eh_valor_percentual:
                nova_lista_empresa_dados.append(valor)
            elif "/" in valor:
                nova_lista_empresa_dados.append(self.validar_data(valor))
            elif not eh_valor_percentual:
                try:
                    nova_lista_empresa_dados.append(float(valor))
                except ValueError:
                    nova_lista_empresa_dados.append(valor)
        return nova_lista_empresa_dados

    def transformar_lista_em_tuples(self, empresa_dados):
        empresa_dados_list = []
        empresa_dados_list.append(tuple(empresa_dados))
        return empresa_dados_list


    def transformar_listas_em_dicionario(self, lista_keys, lista_values):
        novo_dicionario = {lista_keys[i]: lista_values[i] for i in range(len(lista_keys))}
        return novo_dicionario