from src.connect_db.DAConexaoMongo import DAConexaoMongo
from src.dao.mongodb.AbstractMongoDAO import AbstractMongoDAO


class BalancoEmpresaDAO(AbstractMongoDAO):

    def __init__(self, banco_dados="mongodb", nome_colecao="balanco_empresa"):
        super().__init__()
        self.__erro = None
        self.__colecao_mongo = None
        try:
            self.__colecao_mongo = DAConexaoMongo(banco_dados, nome_colecao).get_colecao_mongo()
        except Exception:
            self.__erro = "Falha em estabelecer conexao com a coleção 'balanco_empresa' no MongoDB"

    def inserir_dados(self, balanco_empresa):
        print('** Incluindo dados do balanço...')
        id_balanco_inserido = self.__colecao_mongo.insert_one(balanco_empresa).inserted_id
        return id_balanco_inserido

    def buscar_balanco_empresa_por_papel(self, papel):
        pass

    def buscar_balanco_empresa_por_papel_data(self, papel, data_balanco):
        balanco_papel_data = self.__colecao_mongo.find_one({"Papel": papel,
                                                            "Ult_balanco_processado": data_balanco})
        return balanco_papel_data

    def buscar_balanco_empresa_por_id_empresa_data(self, id_empresa, data_balanco):
        balanco_id_empresa_data = self.__colecao_mongo.find_one({"Id_Empresa": id_empresa,
                                                                 "Ult_balanco_processado": data_balanco})
        return balanco_id_empresa_data

    def buscar_lista_balancos_empresa_por_papel(self, papel):
        lista_balancos = self.__colecao_mongo.find({"Papel": papel})
        return lista_balancos