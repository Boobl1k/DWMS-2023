# Startup

I assume python, java (version 8, not newer) and docker installed in your machine

### 1. Server

add to `/etc/hosts` (or `C:\Windows\System32\drivers\etc\hosts` for windows)

```
#hadoop
127.0.5.1 namenode
127.0.6.1 datanode1
127.0.6.2 datanode2
127.0.6.3 datanode3
127.0.5.2 resourcemanager
127.0.5.3 historyserver
127.0.5.4 nodemanager
```

start the server `docker compose up`
