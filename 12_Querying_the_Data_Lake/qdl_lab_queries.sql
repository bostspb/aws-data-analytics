--
-- Section 1. Transaction table creation query
--
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
) LOCATION 's3://<YOUR_INGEST_BUCKET_NAME>'
TBLPROPERTIES ('has_encrypted_data'='true');


--
-- Section 2. Suspicious table creation query
--
CREATE TABLE "default"."sus_transactions" AS
    SELECT *
    FROM "default"."cc_transactions"
    WHERE transaction_amount > 5000;


--
-- Section 3. Get records over $5000 with an invalid security code.
--
SELECT *
FROM "default"."sus_transactions"
WHERE
    transaction_amount > 5000 AND
    card_sec_code < 100;


--
-- Section 4. Get Diner's Club card purchases over $10,000.
--
SELECT *
FROM "default"."sus_transactions"
WHERE
    transaction_amount > 10000 AND
    card_type like '%Diner%';