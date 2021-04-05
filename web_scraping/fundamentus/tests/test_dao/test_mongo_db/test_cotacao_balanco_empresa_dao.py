import pytest
from web_scraping.fundamentus.src.dao.mongo_db.CotacaoEmpresaDAO import CotacaoEmpresaDAO
from web_scraping.fundamentus.src.dao.mongo_db.BalancoEmpresaDAO import BalancoEmpresaDAO


class TestCotacaoBalancoEmpresaDAO:

    @pytest.fixture(params=[CotacaoEmpresaDAO("test_fundamentus", "cotacao_empresa"),
                            BalancoEmpresaDAO("test_fundamentus", "balanco_empresa")])
    def dados_empresa_mongodb(self, request):
        return request.param

    def test_deve_buscar_dados_de_cotacao_e_balanco_por_papel_e_data_e_retornar_dicionario(self, dados_empresa_mongodb):
        papel_esperado = 'PETR4'
        cotacao_empresa_colecao = dados_empresa_mongodb.buscar_dados_empresa(papel_esperado, '01/03/2021')
        assert str(type(cotacao_empresa_colecao)) == "<class 'dict'>"
        assert cotacao_empresa_colecao['Papel'] == papel_esperado

