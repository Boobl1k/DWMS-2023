# https://pulsar.apache.org/docs/3.1.x/client-libraries-python-use/

import pulsar
from message import Message
from pulsar.schema import AvroSchema

client = pulsar.Client('pulsar://localhost:6650')

try:
    consumer = client.subscribe('message-topic', 'my-subscription', schema=AvroSchema(Message))
    while True:
        message = consumer.receive()
        print(message.value())
        consumer.acknowledge(message)

finally:
    client.close()
