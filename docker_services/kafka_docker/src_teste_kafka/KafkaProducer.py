from confluent_kafka import Producer
import socket
import json

conf = {'bootstrap.servers': "localhost:9092,localhost:9092",
        'client.id': socket.gethostname()}

producer = Producer(conf)

def acked(err, msg):
    if err is not None:
        print("Failed to deliver message: %s: %s" % (str(msg), str(err)))
    else:
        print("Message produced: %s" % (str(msg)))


data = {"nome": "hugo", "idade":31}
data = json.dumps(data).encode('utf-8')

producer.produce(topic="test", key="key", value=data, callback=acked)

# Wait up to 1 second for events. Callbacks will be invoked during
# this method call if the message is acknowledged.
producer.poll(1)