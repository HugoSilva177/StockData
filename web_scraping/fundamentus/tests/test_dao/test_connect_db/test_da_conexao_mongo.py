import pytest
from web_scraping.fundamentus.src.connect_db.DAConexaoMongo import DAConexaoMongo


class TestDAConexaoMongo:

    @pytest.fixture(params=["info_empresa",
                            "cotacao_empresa",
                            "balanco_empresa"])
    def da_conexao_mongo(self, request):
        return DAConexaoMongo(nome_banco="test_fundamentus", nome_colecao=request.param)

    def test_deve_retornar_conexao_com_colecao_no_mongo_db(self, da_conexao_mongo):
        retorno_conexao = da_conexao_mongo.get_colecao_mongo()
        assert str(type(retorno_conexao)) == "<class 'pymongo.collection.Collection'>"
