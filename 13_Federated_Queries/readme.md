# Lab 13. Federated Queries
> City hall has developed a ticketing system to manage citizen requests. Tickets include cases such as notifications 
> of street damage, burned out streetlights, and even noisy establishments. Now, to plan better, city hall wants to 
> use SQL to obtain more insights from these requests, such as the most common problem areas.

## Practice
1. Glue
   1. Crawlers -> Create
      1. Name `ticket-data-crawler`
      2. Add Data Source `DynamoDB`, table `DynamoDBTicketTable`
      3. Choose existing IAM role `AWSGlueServiceRole-lab`
      4. Target database `glue_ticket_db`
   2. Run crawler `ticket-data-crawler`
   3. Data Catalog -> Tables
      1. Review table `glue_ticket_db.dynamodbtickettable`
   4. ETL jobs
      1. Create job with source as `AWS Glue Data Catalog` and target `S3`
         1. For source node: database `glue_ticket_db` and table `dynamodbtickettable` for source node
         2. For target node
            1. format `Parquet`
            2. location `data-lake-bucket-`
            3. Option `Create a table in the Data Catalog and on subsequent runs, update the schema and add new partitions`
            4. Database `glue_ticket_db`
            5. Table `glue-etl-ticket-table`
         3. Job details
            1. Name `ticket-etl-job`
            2. IAM role `AWSGlueServiceRole-lab`
         4. Save & Run job
2. S3
   1. Copy bucket name `data-lake-bucket-442113363817-us-east-1`
3. Athena
   1. Query editor
      1. Data source - AwsDataCatalog
      2. Database - `glue_ticket_db`
      3. Settings -> Manage
         1. Query result location `s3://athena-bucket-442113363817-us-east-1`
      4. Editor 
         1. Run scripts:

```sql
CREATE TABLE AwsDataCatalog.glue_ticket_db.requests
   WITH (external_location = 's3://athena-bucket-442113363817-us-east-1/requests')
   AS SELECT * FROM "glue-etl-ticket-table";
```

```sql
SELECT RequestType, COUNT(* )
FROM "requests"   
GROUP BY RequestType
Order by 2 DESC;
```

4. Athena
   1. Administration -> Data sources -> Create
      1. Choose a data source `Amazon DynamoDB`
      2. Name `athena-federated-dynamodb`
      3. Connection details -> Lambda function `athena_connector_function` 
   2. Query editor -> Editor
      1. Data source - `athena-federated-dynamodb`
      2. Database - `default`
      3. Run scripts:

```sql
SELECT RequestType, COUNT(*)
FROM "athena-federated-dynamodb"."default"."dynamodbtickettable"  
GROUP BY RequestType
Order by 2 DESC;
```

## DIY
1. Athena
   1. Query editor -> Editor
      1. Data source - AwsDataCatalog
      2. Database - `glue_ticket_db`
      3. Run script:
```sql
CREATE TABLE AwsDataCatalog.glue_ticket_db.new_ticket_table
   WITH (external_location = 's3://data-lake-bucket-442113363817-us-east-1/newtable')
   AS SELECT * FROM "athena-federated-dynamodb"."default"."dynamodbtickettable";
```