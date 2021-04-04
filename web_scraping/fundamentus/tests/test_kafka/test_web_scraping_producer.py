import json
import pytest
from confluent_kafka import Consumer
from web_scraping.fundamentus.src.kafka.WebScrapingProducer import WebScrapingProducer


class TestWebScrapingProducer:

    @pytest.fixture
    def instancia_producer(self):
        return WebScrapingProducer()


    @pytest.fixture
    def instancia_consumer(self):
        conf = {'bootstrap.servers': "localhost:9092,localhost:9092",
                'group.id': "etl_fundamentus",
                'auto.offset.reset': 'smallest'}
        return Consumer(conf)

    def test_deve_criar_mensagem_em_um_topic_e_consumir_a_mensagem(self,
                                                                  instancia_producer,
                                                                  instancia_consumer):
        instancia_producer.criar_mensagem_producer("test_fundamentus", {"papel":"PETR4", "empresa":"Petrobras"})
        instancia_consumer.subscribe(["test_fundamentus"])
        mensagem = instancia_consumer.poll(timeout=1.0)
        dados_mensagem = json.loads(mensagem.value().decode('utf-8'))
        assert dados_mensagem == {"papel":"PETR4", "empresa":"Petrobras"}
