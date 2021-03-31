import sys
from confluent_kafka import Consumer
from confluent_kafka.cimpl import KafkaException, KafkaError


class WebScrapingConsumer:

    def __init__(self, topics):
        self.__topics = topics
        conf = {'bootstrap.servers': "localhost:9092,localhost:9092",
                'group.id': "foo",
                'auto.offset.reset': 'smallest'}
        self.__consumer = Consumer(conf)

    def mensagem_dados_empresa_consumer(self):
        try:
            self.__consumer.subscribe(self.__topics)
            mensagem = self.__consumer.poll(timeout=1.0)
            if mensagem is None:
                return None
            if mensagem.error():
                if mensagem.error().code() == KafkaError._PARTITION_EOF:
                    # End of partition event
                    sys.stderr.write('%% %s [%d] reached end at offset %d\n' %
                                        (mensagem.topic(), mensagem.partition(), mensagem.offset()))
                elif mensagem.error():
                    raise KafkaException(mensagem.error())
            else:
                return mensagem
        finally:
            self.__consumer.close()

    def shutdown(self):
        running = False


