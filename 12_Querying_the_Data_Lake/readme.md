# Lab 12. Querying the Data Lake

## Practice
1. Lambda
   1. Open function `Transaction_Generator` -> Test
      1. Create new test event `MyTestEvent` with template `hello-world`
2. S3
   1. Copy bucket name `transaction-ingest-332349894090-153`
3. Athena
   1. Query Editor -> Settings
      1. Browse S3 -> Choose `staging-records-332349894090-153` for location query result
      2. Choose `Encrypt query results` with type `SSE_S3`
   2. Query Editor -> Editor
      1. Run next scripts:

```sql
CREATE EXTERNAL TABLE IF NOT EXISTS `default`.`cc_transactions` (
  `record_number` int,
  `first_name` string,
  `last_name` string,
  `transaction_date` date,
  `card_number` bigint,
  `card_expire` string,
  `card_type` string,
  `card_sec_code` int,
  `transaction_amount` decimal(7,2),
  `user_agent` string
) 
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe' 
WITH SERDEPROPERTIES (
  'serialization.format' = ',',
  'field.delim' = ','
) LOCATION 's3://transaction-ingest-332349894090-153/'
TBLPROPERTIES ('has_encrypted_data'='true');
```

```sql
CREATE TABLE "default"."sus_transactions" AS
    SELECT *
    FROM "default"."cc_transactions"
    WHERE transaction_amount > 5000;
```

```sql
SELECT *
FROM "default"."sus_transactions"
WHERE
    transaction_amount > 5000 AND
    card_sec_code < 100;
```

```sql
SELECT *
FROM "default"."sus_transactions"
WHERE
    transaction_amount > 10000 AND
    card_type like '%Diner%';
```

4. S3
   1. Open bucket `transaction-ingest-332349894090-153`
      1. Review folders `Diners_Club_Suspected/`, `Invalid_Security_Codes/` and `Unsaved/`


## DYI
1. Athena
   1. Query Editor -> Editor
      1. Drop table `sus_transactions`
```sql
DROP TABLE `sus_transactions`;
```