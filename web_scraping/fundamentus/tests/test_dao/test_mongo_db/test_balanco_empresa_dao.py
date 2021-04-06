import pytest
from web_scraping.fundamentus.src.dao.mongo_db.BalancoEmpresaDAO import BalancoEmpresaDAO


class TestBalancoEmpresaDAO:

    @pytest.fixture
    def balanco_empresa_mongodb(self):
        return BalancoEmpresaDAO("test_fundamentus", "balanco_empresa")

    def test_deve_buscar_dados_de_cotacao_e_balanco_por_papel_e_data_e_retornar_dicionario(self, balanco_empresa_mongodb):
        papel_esperado = 'PETR4'
        cotacao_empresa_colecao = balanco_empresa_mongodb.buscar_dados_empresa(papel_esperado, '31/12/2020')
        assert str(type(cotacao_empresa_colecao)) == "<class 'dict'>"
        assert cotacao_empresa_colecao['Papel'] == papel_esperado