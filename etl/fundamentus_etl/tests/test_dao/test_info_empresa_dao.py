import pytest
from etl.fundamentus_etl import InfoEmpresaDAO


class TestInfoEmpresaDAO:

    @pytest.fixture
    def conexao_mongodb(self):
        return InfoEmpresaDAO("test_fundamentus", "info_empresa")

    def test_deve_inserir_dados_no_mongodb_e_retornar_um_objectid(self, conexao_mongodb):
        id_info_empresa_retornado = conexao_mongodb.inserir_dados({"Papel": "PETR4", "Tipo": "PN"})
        assert str(type(id_info_empresa_retornado)) == "<class 'bson.objectid.ObjectId'>"

    def test_deve_buscar_dados_por_papel_e_retornar_dicionario(self, conexao_mongodb):
        papel_esperado = "PETR4"
        conexao_mongodb.inserir_dados({"Papel": papel_esperado, "Tipo": "PN"})
        info_empresa_colecao = conexao_mongodb.buscar_dados_empresa_por_papel(papel_esperado)
        assert str(type(info_empresa_colecao)) == "<class 'dict'>"
        papel_retornado = info_empresa_colecao["Papel"]
        assert papel_retornado == papel_esperado

    def test_deve_buscar_dados_por_id_e_retornar_dicionario(self, conexao_mongodb):
        papel_esperado = "PETR4"
        id_info_empresa_esperado = conexao_mongodb.inserir_dados({"Papel": papel_esperado, "Tipo": "PN"})
        info_empresa_colecao = conexao_mongodb.buscar_dados_empresa_por_id(id_info_empresa_esperado)
        assert str(type(info_empresa_colecao)) == "<class 'dict'>"
        id_info_empresa_buscado = info_empresa_colecao["_id"]
        assert id_info_empresa_buscado == id_info_empresa_esperado






