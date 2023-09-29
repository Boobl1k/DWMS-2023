### 1. startup

add to `/etc/hosts` (or `C:\Windows\System32\drivers\etc\hosts` for windows)

```
#hadoop
127.0.5.1 namenode
127.0.6.1 datanode1
127.0.6.2 datanode2
127.0.6.3 datanode3
127.0.5.2 resourcemanager
127.0.5.4 nodemanager
```

start the server `docker compose up`

### 2. mapreduce

```docker cp dataset namenode:dataset```

```docker cp mapreduce/ namenode:mapreduce/```

```docker exec -it namenode bash```

```hdfs dfs -put /dataset /```

```hadoop jar /mapreduce/java/hadoop-streaming-3.3.6.jar -file /mapreduce/python/mapper.py -mapper /mapreduce/python/mapper.py -file /mapreduce/python/reducer.py -reducer /mapreduce/python/reducer.py -input /dataset -output /output/```
