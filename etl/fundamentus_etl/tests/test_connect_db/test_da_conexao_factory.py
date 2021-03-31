import pytest
from etl.fundamentus_etl import DAConexaoFactory


class TestDAConexaoFactory:

    @pytest.fixture
    def conexao_factory_db(self):
        return DAConexaoFactory()

    def test_deve_retornar_conexao_com_banco_fundamentus_mongodb(self, conexao_factory_db):
        conexao_mongodb_retornado = conexao_factory_db._get_conexao('mongodb_docker', 'mongodb_docker')
        assert str(type(conexao_mongodb_retornado)) == "<class 'pymongo.database.Database'>"