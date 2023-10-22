# Lab 20. Daily Batch Extraction
> A supermarket analytics team would like to run some on-demand queries on the sales tables without
> overloading the OLTP database.
 

## Practice
1. AWS Secrets Manager
   1. `batchdatasalesClusterSecret-vo48OqdJt1mH` -> Secret value -> Retrieve and view the secret value

```json
{
	"dbClusterIdentifier": "sales-database-cluster",
	"password": "YyY=Cs9U,sq.Iio1h-M^1vj8ists01",
	"dbname": "sales",
	"engine": "mysql",
	"port": 3306,
	"host": "sales-database-cluster.cluster-cluppaswsu9q.us-east-1.rds.amazonaws.com",
	"username": "clusteradmin"
}
```

2. RDS
   1. Databases -> `sales-database-cluster` -> `sales-database-instance-writer` -> Connectivity & security
      1. Copy VPC `LabVPC (vpc-0e40ab5995f1b62ae)`
      2. Copy Subnets `subnet-075cc4a430c357e05`, `subnet-0a1503f98a2a15138`
      3. VPC security groups `Database Security Group (sg-0d181e4ef3fc08274)`
         1. Inbound rules -> Edit -> Add rule
            1. Type `All TCP`
            2. Source `Custom` -> `Database Security Group (sg-0d181e4ef3fc08274)`
3. Glue
   1. Databases -> Add-> `batch-db`
   2. Connections -> Create connection
      1. Name `batch-conn`
      2. Type `Amazon RDS`
      3. Engine `Aurora`
      4. Connection access
         1. Database instance `sales-database-instance-writer`
         2. Database name `sales`
         3. Username `clusteradmin`
         4. Password `YyY=Cs9U,sq.Iio1h-M^1vj8ists01`
   3. Connections -> `batch-conn` -> Edit
      1. Password `YyY=Cs9U,sq.Iio1h-M^1vj8ists01`
      2. VPC `vpc-0e40ab5995f1b62ae`
      3. Subnet `subnet-075cc4a430c357e05`
      4. Security group `sg-0d181e4ef3fc08274`
   4. Tables -> Add tables using crawler
      1. Name `batch-db-table`
      2. Add data source 
         1. Data source`JDBC`
         2. Connection `batch-conn`
         3. Path `sales/%`
      3. IAM role `GlueRole-*`
      4. Target database `batch-db`
      5. Crawler schedule -> Frequency -> On demand
      6. Save & Run
   5. Tables -> Review new tables
      1. `batch-db.sales_customers`
      2. `batch-db.sales_transactions`
   6. ETL jobs -> Create job -> Visual ETL
      1. Add node `AWS Glue Data Catalog`
         1. Name `Customer Table`
         2. Database `batch-db`
         3. Table `sales_customers`
      2. Add node `Change Schema`
         1. Drop attribute `dob`
      3. Add node `Amazon S3` (target)
         1. Format `Parquet`
         2. Compression `Snappy`
         3. S3 Target Location `s3://raw-bucket-332349894090-205`
         4. Data Catalog update options -> Create a table in the Data Catalog and on subsequent runs, keep existing schema and add new partitions
            1. Database `batch-db`
            2. Table `customers`
      4. Job details
         1. Name `Customers_Job`
         2. IAM role `GlueRole-*`
         3. Requested number of workers - 3
         4. Number of retries - 1
         5. Job timeout (minutes) - 5
         6. Save & Run
4. Athena
   1. Query editor
      1. Settings -> Manage -> Location of query result -> `s3://processed-bucket-332349894090-205`
   2. Preview table `AwsDataCatalog.batch-db.customers`


## DIY
1. Glue
   1. ETL jobs -> Create job -> Visual ETL
      1. Add node `AWS Glue Data Catalog`
         1. Name `Transactions Table`
         2. Database `batch-db`
         3. Table `sales_customers` 
      2. Add node `Amazon S3` (target)
         1. Format `Parquet`
         2. Compression `Snappy`
         3. S3 Target Location `s3://raw-bucket-332349894090-205`
         4. Data Catalog update options -> Create a table in the Data Catalog and on subsequent runs, keep existing schema and add new partitions
            1. Database `batch-db`
            2. Table `transactions`
      3. Job details
         1. Name `Transactions_Job`
         2. IAM role `GlueRole-*`
         3. Requested number of workers - 3
         4. Number of retries - 1
         5. Job timeout (minutes) - 5
         6. Save & Run
2. Athena
   1. Preview table `AwsDataCatalog.batch-db.transactions`