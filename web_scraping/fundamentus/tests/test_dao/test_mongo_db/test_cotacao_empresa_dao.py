import pytest
from web_scraping.fundamentus.src.dao.mongo_db.CotacaoEmpresaDAO import CotacaoEmpresaDAO


class TestCotacaoBalancoEmpresaDAO:

    @pytest.fixture
    def cotacao_empresa_mongodb(self, ):
        return CotacaoEmpresaDAO("test_fundamentus", "cotacao_empresa")

    def test_deve_buscar_dados_de_cotacao_e_balanco_por_papel_e_data_e_retornar_dicionario(self, cotacao_empresa_mongodb):
        papel_esperado = 'PETR4'
        cotacao_empresa_colecao = cotacao_empresa_mongodb.buscar_dados_empresa(papel_esperado, '01/03/2021')
        assert str(type(cotacao_empresa_colecao)) == "<class 'dict'>"
        assert cotacao_empresa_colecao['Papel'] == papel_esperado

