import pytest
from bson.objectid import ObjectId
from extract_transform_load.fundamentus_etl.src.etl.ProcessoETL import ProcessoETL

from extract_transform_load.fundamentus_etl.src.dao.mongodb.IndicadoresDAO import IndicadoresDAO
from extract_transform_load.fundamentus_etl.src.dao.mongodb.InfoEmpresaDAO import InfoEmpresaDAO
from extract_transform_load.fundamentus_etl.src.dao.mongodb.BalancoEmpresaDAO import BalancoEmpresaDAO
from extract_transform_load.fundamentus_etl.src.dao.mongodb.CotacaoEmpresaDAO import CotacaoEmpresaDAO
from extract_transform_load.fundamentus_etl.src.dao.mongodb.OscilacoesEmpresaDAO import OscilacoesEmpresaDAO

from extract_transform_load.fundamentus_etl.src.dao.hadoop_hdfs.InfoEmpresaHDFS import InfoEmpresaHDFS
from extract_transform_load.fundamentus_etl.src.dao.hadoop_hdfs.CotacaoEmpresaHDFS import CotacaoEmpresaHDFS
from extract_transform_load.fundamentus_etl.src.dao.hadoop_hdfs.BalancoEmpresaHDFS import BalancoEmpresaHDFS
from extract_transform_load.fundamentus_etl.src.dao.hadoop_hdfs.OscilacoesEmpresaHDFS import OscilacoesEmpresaHDFS
from extract_transform_load.fundamentus_etl.src.dao.hadoop_hdfs.IndicadoresEmpresaHDFS import IndicadoresEmpresaHDFS


class TestProcessoETL:

    @pytest.fixture(params=[(InfoEmpresaDAO(banco_dados="test_fundamentus"), InfoEmpresaHDFS()),
                            (CotacaoEmpresaDAO(banco_dados="test_fundamentus"), CotacaoEmpresaHDFS()),
                            (OscilacoesEmpresaDAO(banco_dados="test_fundamentus"), OscilacoesEmpresaHDFS()),
                            (IndicadoresDAO(banco_dados="test_fundamentus"), IndicadoresEmpresaHDFS()),
                            (BalancoEmpresaDAO(banco_dados="test_fundamentus"), BalancoEmpresaHDFS())])
    def processo_etl_scraping(self, request):
        return request.param

    @pytest.fixture
    def processo_etl(self, processo_etl_scraping):
        return ProcessoETL(processo_etl_scraping[0], processo_etl_scraping[1])

    def dados_empresa(self):
        return {"dados_label":['Papel', 'Tipo'], "dados_valores":['PETR4', 'PN']}

    def test_extrair_deve_retornar_lista_labels_e_lista_valores_do_tipo_list(self, processo_etl, dados_empresa):
        lista_label, lista_valores = processo_etl._extrair_dados_empresa(dados_empresa)
        assert str(type(lista_label)) == "<class 'list'>"
        assert str(type(lista_valores)) == "<class 'list'>"

    def test_extrair_deve_retornar_duas_litas_do_mesmo_tamanho(self, processo_etl, dados_empresa):
        lista_labels, lista_valores = processo_etl._extrair_dados_empresa(dados_empresa)
        assert len(lista_labels) == len(lista_valores)

    def test_transformar_deve_receber_duas_listas_e_retornar_um_dicionario_e_um_spark_dataframe(self,
                                                                                                processo_etl,
                                                                                                dados_empresa):
        dados_empresa_dicionario, dados_empresa_spark_df = processo_etl._transformar_dados_empresa(
                                                                                        dados_empresa["dados_label"],
                                                                                        dados_empresa["dados_valores"])
        assert str(type(dados_empresa_dicionario)) == "<class 'dict'>"
        assert str(type(dados_empresa_spark_df)) == "<class 'pyspark.sql.dataframe.DataFrame'>"

    #def test_gravar_deve_retornar_um_tipo_objectid(self, mongodb, processo_etl):
        #object_id_retornado = mongodb.test_info_empresa.insert_one({'Papel':'PETR4', 'Tipo': 'PN'}).inserted_id
        #assert str(type(object_id_retornado)) == "<class 'bson.objectid.ObjectId'>"
