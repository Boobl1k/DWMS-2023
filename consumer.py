# https://pulsar.apache.org/docs/3.1.x/client-libraries-python-use/

import pulsar

client = pulsar.Client('pulsar://localhost:6650')

try:
    consumer = client.subscribe('my-topic', 'my-subscription')
    while True:
        json_message = consumer.receive().data()
        print(json_message)

finally:
    client.close()
