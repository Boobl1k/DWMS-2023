```sql
LOAD CSV WITH HEADERS FROM 'file:///twich_short.csv' as row
CREATE (subscriber:User {id: toInteger(row.numeric_id_1)})
CREATE (streamer:User {id: toInteger(row.numeric_id_2)})
CREATE (subscriber)-[:SUBSCRIBED_TO]->(streamer);
```

```sql
CALL gds.graph.project(
    'twich_subscriptions',
    'User',
    'SUBSCRIBED_TO'
);
```

```sql
CALL gds.pageRank.stream(
    'twich_subscriptions',
    {
        maxIterations: 10000,
        dampingFactor: 0.95
    }
)
YIELD nodeId, score
RETURN nodeId, score
ORDER BY score DESC
LIMIT 500;
```

```sql
MATCH (n)-[r]->(m)
RETURN n, r, m
LIMIT 20000;
```
