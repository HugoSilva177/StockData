import pytest
from src.connect_db.DAConexaoFactory import DAConexaoFactory


class TestDAConexaoFactory:

    @pytest.fixture
    def conexao_factory_db(self):
        return DAConexaoFactory()

    def test_deve_retornar_conexao_com_banco_fundamentus_mongodb(self, conexao_factory_db):
        conexao_mongodb_retornado = conexao_factory_db._get_conexao('mongodb', 'mongodb')
        assert str(type(conexao_mongodb_retornado)) == "<class 'pymongo.database.Database'>"