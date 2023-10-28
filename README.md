### 4 pulsar

1. ```docker compose up```
2. ```./producer.py```
3. ```./consumer.py```
4. send some messages
5. stop both consumer and producer
6. ```docker exec -it broker bash```
7. update schema compability ```/pulsar/bin/pulsar-admin namespaces set-schema-compatibility-strategy --compatibility FORWARD_TRANSITIVE public/default```
8. update ```message.py``` (uncomment line)
9. ```./producer.py```
10. ```./consumer.py```
11. send message, verify new field consumed
12. verify schema versions  
```/pulsar/bin/pulsar-admin schemas get --version 0 persistent://public/default/message-topic```  
```/pulsar/bin/pulsar-admin schemas get persistent://public/default/message-topic```  
