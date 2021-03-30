import json
import socket
from confluent_kafka import Producer


class WebScrapingProducer:

    def __init__(self):
        conf = {'bootstrap.servers': "localhost:9092,localhost:9092",
                'client.id': socket.gethostname()}
        self.__producer = Producer(conf)

    def criar_mensagem_producer(self, topic, dados_empresa):
        dados_empresa = json.dumps(dados_empresa).encode('utf-8')

        self.__producer.produce(topic=topic,
                                key="key",
                                value=dados_empresa,
                                callback=self.__retorno_resultado_mensagem_producer)

        # Wait up to 1 second for events. Callbacks will be invoked during
        # this method call if the message is acknowledged.
        self.__producer.poll(1)

    def __retorno_resultado_mensagem_producer(self, err, dados_empresa):
        if err is not None:
            print("Failed to deliver message: %s: %s" % (str(dados_empresa), str(err)))
        else:
            print("Message produced: %s" % (str(dados_empresa)))
