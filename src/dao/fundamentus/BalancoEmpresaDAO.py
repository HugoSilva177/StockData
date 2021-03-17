from src.connect_db.DAConexaoMongo import DAConexaoMongo
from src.dao.fundamentus.AbstractMongoDAO import AbstractMongoDAO


class BalancoEmpresaDAO(AbstractMongoDAO):

    def __init__(self):
        super().__init__()
        self.__erro = None
        self.__colecao_mongo = None
        try:
            self.__colecao_mongo = DAConexaoMongo('fundamentus', 'balanco_empresa').get_colecao_mongo()
        except Exception:
            self.__erro = "Falha em estabelecer conexao com a coleção 'balanco_empresa' no MongoDB"

    def inserir_dados(self, balanco_empresa):
        id_balanco_inserido = self.__colecao_mongo.insert_one(balanco_empresa).inserted_id
        return id_balanco_inserido

    def buscar_balanco_empresa_por_papel(self, papel):
        pass

    def buscar_balanco_empresa_por_papel_data(self, papel, data_balanco):
        balanco_papel_data = self.__colecao_mongo.find_one({"Papel": papel,
                                                            "Data_ult_cot": data_balanco})
        return balanco_papel_data

    def buscar_lista_balancos_empresa_por_papel(self, papel):
        lista_balancos = self.__colecao_mongo.find({"Papel": papel})
        return lista_balancos

    def atualizar_cotacoes_no_balanco_por_id(self, id_inserido_balanco, id_inserido_cotacao):
        pass

    def atualizar_cotacoes_no_balanco_por_papel_data(self, papel, data_ult_balanco, id_inserido_cotacao):
        pass