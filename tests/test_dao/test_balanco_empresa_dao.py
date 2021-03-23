import pytest
from src.dao.fundamentus.BalancoEmpresaDAO import BalancoEmpresaDAO
from src.dao.fundamentus.InfoEmpresaDAO import InfoEmpresaDAO


class TestBalancoEmpresaDAO:

    @pytest.fixture
    def balanco_empresa_mongodb(self):
        return BalancoEmpresaDAO("test_fundamentus", "balanco_empresa")


    @pytest.fixture
    def info_empresa_mongodb(self):
        return InfoEmpresaDAO("test_fundamentus", "info_empresa")

    def test_deve_inserir_dados_balanco_apos_incluir_dados_da_empresa_e_retornar_objectid(self,
                                                                                          balanco_empresa_mongodb,
                                                                                          info_empresa_mongodb):
        id_info_empresa_inserido = info_empresa_mongodb.inserir_dados({"Papel": "PETR4",
                                                                       "Tipo": "PN"})
        assert str(type(id_info_empresa_inserido)) == "<class 'bson.objectid.ObjectId'>"
        id_balanco_inserido = balanco_empresa_mongodb.inserir_dados({"Id_Empresa": id_info_empresa_inserido,
                                                                    "Papel": "PETR4",
                                                                    "Valor_da_firma":"635.075.000.000",
                                                                    "Ativo":"987.419.000.000"})
        assert str(type(id_balanco_inserido)) == "<class 'bson.objectid.ObjectId'>"