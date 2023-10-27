# https://pulsar.apache.org/docs/3.1.x/client-libraries-python-use/

import pulsar
import random
import sys
import json

client = pulsar.Client('pulsar://localhost:6650')

try:
    producer = client.create_producer('my-topic')

    id = 1
    for line in sys.stdin:
        line = line.strip()
        message = {
            "id": id,
            "text": line
        }
        if line == "add_field":
            message["extra"] = random.randrange(1,6)
        json_message = json.dumps(message)
        print(json_message)
        producer.send(json_message.encode('utf-8'))
        id += 1

finally:
    client.close()
