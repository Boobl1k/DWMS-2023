from pulsar.schema import Record, String, Integer


class Order(Record):
    product_name = String()
    price = Integer()
