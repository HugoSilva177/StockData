import pytest
from web_scraping.fundamentus.src.dao.mongo_db.InfoEmpresaDAO import InfoEmpresaDAO


class TestInfoEmpresaDAO:

    @pytest.fixture
    def conexao_mongodb(self):
        return InfoEmpresaDAO("test_fundamentus", "info_empresa")

    def test_deve_buscar_dados_da_empresa_por_papel_e_retornar_dicionario_se_dados_existir(self, conexao_mongodb):
        papel_esperado = "PETR4"
        info_empresa_colecao = conexao_mongodb.buscar_dados_empresa(papel_esperado)
        assert str(type(info_empresa_colecao)) == "<class 'dict'>"
        papel_retornado = info_empresa_colecao["Papel"]
        assert papel_retornado == papel_esperado

    def test_deve_buscar_dados_da_empresa_por_papel_e_retornar_nonetype_se_dados_nao_existir(self, conexao_mongodb):
        papel_nao_existente = "PETR"
        info_empresa_colecao = conexao_mongodb.buscar_dados_empresa(papel_nao_existente)
        assert str(type(info_empresa_colecao)) == "<class 'NoneType'>"
