import pytest
from extract_transform_load.fundamentus_etl import InfoEmpresaDAO


class TestInfoEmpresaDAO:

    @pytest.fixture
    def conexao_mongodb(self):
        return InfoEmpresaDAO("test_fundamentus", "info_empresa")

    def test_deve_inserir_dados_no_mongodb_e_retornar_um_objectid(self, conexao_mongodb):
        id_info_empresa_retornado = conexao_mongodb.inserir_dados({"Papel": "PETR4", "Tipo": "PN"})
        assert str(type(id_info_empresa_retornado)) == "<class 'bson.objectid.ObjectId'>"







