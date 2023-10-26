### 3. hive

add to `/etc/hosts` (or `C:\Windows\System32\drivers\etc\hosts` for windows)

```
#hadoop
127.0.0.1 namenode
127.0.0.1 datanode
```

```sql
create database if not exists testdb;
use testdb;
create table netflix (
    user_id integer,
    rating integer,
    date_created DATE
) 
row format delimited 
fields terminated by ',' 
lines terminated by '\n' 
stored as textfile location 'hdfs://namenode:8020/hive';
```

```hdfs dfs -put /hive /hive/```

```sql
select * from 
        (
        SELECT *,ROW_NUMBER() over () as rowid FROM netflix
        )t 
    where rowid > 0 and rowid <=20;
```

```sql
select year, avg(rating) from (
    select *, date_format(date_created, 'yyyy') as year from netflix
)t group by year;
```
