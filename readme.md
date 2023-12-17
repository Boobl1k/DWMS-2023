
```sh
/pulsar/bin/pulsar-admin topics create public/default/test-topic
```

```sh
/pulsar/bin/pulsar-admin sinks create \
  --tenant "public" \
  --sink-type 'jdbc-clickhouse' \
  --name 'orders-connector' \
  --inputs "persistent://public/default/test-topic" \
  --parallelism 1 \
  --sink-config-file /connector-config.yaml
```

```sql
CREATE TABLE orders
(
    product_name String,
    price        INTEGER
) ENGINE = MergeTree()
      ORDER BY product_name;

CREATE TABLE orders_aggregated
(
    product_name  String,
    total_price   INTEGER
) ENGINE = SummingMergeTree()
      ORDER BY product_name;

CREATE MATERIALIZED VIEW orders_mv TO orders_aggregated AS
SELECT product_name,
       sum(price) as total_price
FROM orders
GROUP BY product_name;

```
