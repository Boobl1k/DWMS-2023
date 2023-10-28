from pulsar.schema import Record, String, Integer

class Message(Record):
    id = Integer()
    text = String()
    #extra = String()