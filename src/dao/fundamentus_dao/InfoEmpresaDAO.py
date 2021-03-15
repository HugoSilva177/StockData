from src.connect_db.DAConexaoMongo import DAConexaoMongo


class InfoEmpresaDAO:

    def __init__(self):
        self.__erro = None
        self.__colecao_mongo = None
        try:
            self.__colecao_mongo = DAConexaoMongo('fundamentus', 'info_empresa').get_colecao_mongo()
        except Exception:
            self.__erro = "Falha em estabelecer conexao com a coleção 'dados_empresa' no MongoDB"

    def buscar_dados_empresa_por_papel(self, papel):
        dados_empresa = self.__colecao_mongo.find_one({"Papel": papel})
        return dados_empresa

    def inserir_dados_empresa(self, info_empresa):
        self.__colecao_mongo.insert_one(info_empresa)

    def get_erro(self):
        return self.__erro