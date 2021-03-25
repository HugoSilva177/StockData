import pytest
from fundamentus_etl.src.dao.mongodb.IndicadoresDAO import IndicadoresDAO
from fundamentus_etl.src.dao.mongodb.CotacaoEmpresaDAO import CotacaoEmpresaDAO


class TestIndicadoresEmpresaDAO:

    @pytest.fixture
    def cotacao_empresa_mongodb(self):
        return CotacaoEmpresaDAO("test_fundamentus", "cotacao_empresa")

    @pytest.fixture
    def indicadores_empresa_mongodb(self):
        return IndicadoresDAO("test_fundamentus", "indicadores_empresa")


    def test_deve_inserir_dados_de_indicadores_apos_inserir_dados_de_cotacao_e_retornar_objectid(self,
                                                                                                cotacao_empresa_mongodb,
                                                                                                indicadores_empresa_mongodb):
        id_cotacao_inserido = cotacao_empresa_mongodb.inserir_dados({"Papel":"PETR4",
                                                                     "Cotacao":"23,52"})
        assert str(type(id_cotacao_inserido)) == "<class 'bson.objectid.ObjectId'>"
        id_indicadores_inserido = indicadores_empresa_mongodb.inserir_dados({
                                                  "Id_Cotacao":id_cotacao_inserido,
                                                  "Papel":"PETR4",
                                                  "P/L":"43,16",
                                                  "LPA":"0,54"})
        assert str(type(id_indicadores_inserido)) == "<class 'bson.objectid.ObjectId'>"