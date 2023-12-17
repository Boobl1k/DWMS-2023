import pulsar
import sys
from order import Order
import random
import time


client = pulsar.Client(
    "pulsar://localhost:6650",
    authentication=pulsar.AuthenticationBasic(
        username="admin", password="apachepulsar"
    ),
)
TOPIC_NAME = "persistent://public/default/test-topic"

producer = client.create_producer(
    topic="persistent://public/default/test-topic",
    schema=pulsar.schema.JsonSchema(Order),
)

products = ['a', 'b', 'c']

while True:
    order = Order(product_name=products[random.randint(0, 2)], price = random.randint(20, 100))
    producer.send(order)
    time.sleep(1)
