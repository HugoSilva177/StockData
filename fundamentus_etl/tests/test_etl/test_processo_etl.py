import pytest
from bson.objectid import ObjectId
from fundamentus_etl.src.etl.ProcessoETL import ProcessoETL
from fundamentus_etl.src.dao.mongodb.IndicadoresDAO import IndicadoresDAO
from fundamentus_etl.src.dao.mongodb.InfoEmpresaDAO import InfoEmpresaDAO
from fundamentus_etl.src.dao.mongodb.CotacaoEmpresaDAO import CotacaoEmpresaDAO
from fundamentus_etl.src.dao.hadoop_hdfs.InfoEmpresaHDFS import InfoEmpresaHDFS
from fundamentus_etl.src.dao.mongodb.BalancoEmpresaDAO import BalancoEmpresaDAO
from fundamentus_etl.src.dao.hadoop_hdfs.CotacaoEmpresaHDFS import CotacaoEmpresaHDFS
from fundamentus_etl.src.dao.mongodb.OscilacoesEmpresaDAO import OscilacoesEmpresaDAO
from fundamentus_etl.src.dao.hadoop_hdfs.BalancoEmpresaHDFS import BalancoEmpresaHDFS
from fundamentus_etl.src.dao.hadoop_hdfs.OscilacoesEmpresaHDFS import OscilacoesEmpresaHDFS
from fundamentus_etl.src.dao.hadoop_hdfs.IndicadoresEmpresaHDFS import IndicadoresEmpresaHDFS
from fundamentus_etl.src.web_scraping.fundamentus_web.InfoEmpresaScraping import InfoEmpresaScraping
from fundamentus_etl.src.web_scraping.fundamentus_web.BalancoEmpresaScraping import BalancoEmpresaScraping
from fundamentus_etl.src.web_scraping.fundamentus_web.CotacaoEmpresaScraping import CotacaoEmpresaScraping
from fundamentus_etl.src.web_scraping.fundamentus_web.OscilacoesEmpresaScraping import OscilacoesEmpresaScraping
from fundamentus_etl.src.web_scraping.fundamentus_web.IndicadoresEmpresaScraping import IndicadoresEmpresaScraping


class TestProcessoETL:

    @pytest.fixture(params=[(InfoEmpresaScraping("PETR4"), InfoEmpresaDAO(), InfoEmpresaHDFS()),
                            (CotacaoEmpresaScraping("PETR4"), CotacaoEmpresaDAO(), CotacaoEmpresaHDFS()),
                            (OscilacoesEmpresaScraping("PETR4"), OscilacoesEmpresaDAO(ObjectId()), OscilacoesEmpresaHDFS()),
                            (IndicadoresEmpresaScraping("PETR4"), IndicadoresDAO(ObjectId()), IndicadoresEmpresaHDFS()),
                            (BalancoEmpresaScraping("PETR4"), BalancoEmpresaDAO(), BalancoEmpresaHDFS())])
    def processo_etl_scraping(self, request):
        return request.param

    @pytest.fixture
    def processo_etl(self, processo_etl_scraping):
        return ProcessoETL(processo_etl_scraping[0], processo_etl_scraping[1], processo_etl_scraping[2])

    def test_extrair_deve_retornar_lista_labels_e_lista_valores_do_tipo_list(self, processo_etl):
        lista_label, lista_valores = processo_etl._extrair_dados_empresa([], [])
        assert str(type(lista_label)) == "<class 'list'>"
        assert str(type(lista_valores)) == "<class 'list'>"

    def test_extrair_deve_retornar_duas_listas(self, processo_etl):
        listas_retornadas = processo_etl._extrair_dados_empresa([], [])
        quantidade_listas_esperadas = 2
        assert len(listas_retornadas) == quantidade_listas_esperadas

    def test_extrair_deve_retornar_mesmo_tamanho_de_listas(self, processo_etl):
        lista_labels, lista_valores = processo_etl._extrair_dados_empresa([], [])
        assert len(lista_labels) == len(lista_valores)

    def test_transformar_deve_receber_duas_listas_e_retornar_um_dicionario_e_um_spark_dataframe(self, processo_etl):
        dicionario_spark_df_retornado = processo_etl._transformar_dados_empresa(['label1', 'label2'], ['valor1',
                                                                                                       'valor2'])
        assert str(type(dicionario_spark_df_retornado[0])) == "<class 'dict'>"
        assert str(type(dicionario_spark_df_retornado[1])) == "<class 'pyspark.sql.dataframe.DataFrame'>"

    def test_gravar_deve_retornar_um_tipo_objectid(self, mongodb, processo_etl):
        object_id_retornado = mongodb.test_info_empresa.insert_one({'Papel':'PETR4', 'Tipo': 'PN'}).inserted_id
        assert str(type(object_id_retornado)) == "<class 'bson.objectid.ObjectId'>"
