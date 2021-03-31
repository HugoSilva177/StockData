import pytest
from extract_transform_load.fundamentus_etl.src.dao.mongodb.CotacaoEmpresaDAO import CotacaoEmpresaDAO
from extract_transform_load.fundamentus_etl import OscilacoesEmpresaDAO
from extract_transform_load.fundamentus_etl import IndicadoresDAO
from extract_transform_load.fundamentus_etl import InfoEmpresaDAO


class TestCotacaoEmpresaDAO:

    @pytest.fixture
    def cotacao_empresa_mongodb(self):
        return CotacaoEmpresaDAO("test_fundamentus", "cotacao_empresa")

    @pytest.fixture
    def info_empresa_mongodb(self):
        return InfoEmpresaDAO("test_fundamentus", "info_empresa")

    @pytest.fixture
    def oscilacoes_empresa_mongodb(self):
        return OscilacoesEmpresaDAO("test_fundamentus", "oscilacoes_empresa")

    @pytest.fixture
    def indicadores_empresa_mongodb(self):
        return IndicadoresDAO("test_fundamentus", "indicadores_empresa")

    def test_deve_inserir_dados_cotacao_apos_incluir_dados_da_empresa_e_retornar_objectid(self,
                                                                                          cotacao_empresa_mongodb,
                                                                                          info_empresa_mongodb):
        id_info_empresa_inserido = info_empresa_mongodb.inserir_dados({"Papel": "PETR4", "Tipo": "PN"})
        assert str(type(id_info_empresa_inserido)) == "<class 'bson.objectid.ObjectId'>"
        id_cotacao_inserido = cotacao_empresa_mongodb.inserir_dados({"Id_Empresa": id_info_empresa_inserido,
                                                                    "Papel": "PETR4",
                                                                    "Cotacao": "24,00"})
        assert str(type(id_cotacao_inserido)) == "<class 'bson.objectid.ObjectId'>"

    def test_deve_inserir_dados_oscilacoes_na_colecao_cotacao(self,
                                                              cotacao_empresa_mongodb,
                                                              oscilacoes_empresa_mongodb):
        id_cotacao_inserido = cotacao_empresa_mongodb.inserir_dados({"Papel": "GGBR4",
                                                                     "Cotacao": "24,00"})
        id_oscilacoes_esperado = oscilacoes_empresa_mongodb.inserir_dados({"Papel":"GGBR4",
                                                                           "Oscilacoes_Dia":"-2,00%"})
        cotacao_empresa_mongodb.inserir_oscilacoes_na_cotacao(id_cotacao_inserido,
                                                              id_oscilacoes_esperado)
        cotacao = cotacao_empresa_mongodb.buscar_cotacao_empresa_por_id_cotacao(id_cotacao_inserido)
        id_oscilacoes_inserido = cotacao["Oscilacao"]
        assert id_oscilacoes_inserido == id_oscilacoes_esperado

    def test_deve_inserir_dados_indicadores_na_colecao_cotacao(self,
                                                               cotacao_empresa_mongodb,
                                                               indicadores_empresa_mongodb):
        id_cotacao_inserido = cotacao_empresa_mongodb.inserir_dados({"Papel": "GGBR4",
                                                                     "Cotacao": "24,00"})
        id_indicadores_esperado = indicadores_empresa_mongodb.inserir_dados({"Papel":"PETR4",
                                                   "P/L":"43,16",
                                                   "LPA":"0,54"})
        cotacao_empresa_mongodb.inserir_indicadores_na_cotacao(id_cotacao_inserido,
                                                               id_indicadores_esperado)
        cotacao = cotacao_empresa_mongodb.buscar_cotacao_empresa_por_id_cotacao(id_cotacao_inserido)
        id_indicadores_inserido = cotacao["Indicador_Fundamentalista"]
        assert id_indicadores_inserido == id_indicadores_esperado
