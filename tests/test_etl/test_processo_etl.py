import pytest
from bson.objectid import ObjectId
from src.etl.ProcessoETL import ProcessoETL
from src.dao.fundamentus.IndicadoresDAO import IndicadoresDAO
from src.dao.fundamentus.InfoEmpresaDAO import InfoEmpresaDAO
from src.dao.fundamentus.CotacaoEmpresaDAO import CotacaoEmpresaDAO
from src.dao.fundamentus.BalancoEmpresaDAO import BalancoEmpresaDAO
from src.dao.fundamentus.OscilacoesEmpresaDAO import OscilacoesEmpresaDAO
from src.web_scraping.fundamentus_web.InfoEmpresaScraping import InfoEmpresaScraping
from src.web_scraping.fundamentus_web.BalancoEmpresaScraping import BalancoEmpresaScraping
from src.web_scraping.fundamentus_web.CotacaoEmpresaScraping import CotacaoEmpresaScraping
from src.web_scraping.fundamentus_web.OscilacoesEmpresaScraping import OscilacoesEmpresaScraping
from src.web_scraping.fundamentus_web.IndicadoresEmpresaScraping import IndicadoresEmpresaScraping


class TestProcessoETL:

    @pytest.fixture(params=[(InfoEmpresaScraping("PETR4"), InfoEmpresaDAO()),
                            (CotacaoEmpresaScraping("PETR4"), CotacaoEmpresaDAO()),
                            (OscilacoesEmpresaScraping("PETR4"), OscilacoesEmpresaDAO(ObjectId())),
                            (IndicadoresEmpresaScraping("PETR4"), IndicadoresDAO(ObjectId())),
                            (BalancoEmpresaScraping("PETR4"), BalancoEmpresaDAO())])
    def processo_etl_scraping(self, request):
        return request.param


    @pytest.fixture
    def processo_etl(self, processo_etl_scraping):
        return ProcessoETL(processo_etl_scraping[0], processo_etl_scraping[1])

    def test_deve_extrair_e_retornar_lista_labels_e_lista_valores_do_tipo_list(self, processo_etl):
        lista_label, lista_valores = processo_etl._extrair_dados_empresa([], [])
        assert str(type(lista_label)) == "<class 'list'>"
        assert str(type(lista_valores)) == "<class 'list'>"

    def test_deve_extrair_e_retornar_duas_listas(self, processo_etl):
        listas_retornadas = processo_etl._extrair_dados_empresa([], [])
        quantidade_listas_esperadas = 2
        assert len(listas_retornadas) == quantidade_listas_esperadas

    def test_deve_extrair_e_retornar_mesmo_tamanho_de_listas(self, processo_etl):
        lista_labels, lista_valores = processo_etl._extrair_dados_empresa([], [])
        assert len(lista_labels) == len(lista_valores)

    def test_deve_transformar_e_receber_duas_listas_e_retornar_um_tipo_dicionario(self, processo_etl):
        dicionario_retornado = processo_etl._transformar_dados_empresa(['label1', 'label2'], ['valor1', 'valor2'])
        assert str(type(dicionario_retornado)) == "<class 'dict'>"

    def test_deve_gravar_e_retornar_um_tipo_objectid(self, mongodb, processo_etl):
        object_id_retornado = mongodb.test_info_empresa.insert_one({'Papel':'PETR4', 'Tipo': 'PN'}).inserted_id
        assert str(type(object_id_retornado)) == "<class 'bson.objectid.ObjectId'>"
