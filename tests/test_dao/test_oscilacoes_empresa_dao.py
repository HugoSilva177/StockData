import pytest
from src.dao.fundamentus.OscilacoesEmpresaDAO import OscilacoesEmpresaDAO
from src.dao.fundamentus.CotacaoEmpresaDAO import CotacaoEmpresaDAO


class TestOscilacoesEmpresaDAO:

    @pytest.fixture
    def cotacao_empresa_mongodb(self):
        return CotacaoEmpresaDAO("test_fundamentus", "cotacao_empresa")

    @pytest.fixture
    def oscilacoes_empresa_mongodb(self):
        return OscilacoesEmpresaDAO("test_fundamentus", "oscilacoes_empresa")


    def test_deve_inserir_dados_de_oscilacoes_apos_inserir_dados_de_cotacao_e_retornar_objectid(self,
                                                                            cotacao_empresa_mongodb,
                                                                            oscilacoes_empresa_mongodb):
        id_cotacao_inserido = cotacao_empresa_mongodb.inserir_dados({"Papel":"PETR4",
                                                                     "Cotacao":"23,52"})
        assert str(type(id_cotacao_inserido)) == "<class 'bson.objectid.ObjectId'>"
        id_oscilacoes_inserido = oscilacoes_empresa_mongodb.inserir_dados({"Id_Cotacao":id_cotacao_inserido,
                                                  "Papel":"PETR4",
                                                  "Oscilacoes_Dia":"-2,00%"})
        assert str(type(id_oscilacoes_inserido)) == "<class 'bson.objectid.ObjectId'>"
