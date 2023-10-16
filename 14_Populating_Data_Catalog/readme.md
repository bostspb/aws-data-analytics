# Lab 14. Populating Data Catalog

## Practice
1. S3
   1. Copy bucket name `raw-data-442113363817-cdd2b590`
   2. Review object `raw-data-442113363817-cdd2b590/inventory.csv`
2. Glue
   1. Databases -> Add `inventory-db`
   2. Tables -> Add table using crawler
      1. Crawler name `inventory-crawler`
      2. Add data source `S3` with bucket `raw-data-442113363817-cdd2b590`
      3. IAM role `aws_glue_role`
      4. Target database `inventory-db`
   3. Crawlers
      1. Run crawler
   4. Tables
      1. Review table `raw_data_442113363817_cdd2b590`
3. Athena
   1. Query editor
      1. Settings -> Manage
         1. Query result location `s3://athena-results-442113363817-cdd2b590`
   2. Editor
      1. Data source - AwsDataCatalog
      2. Database - `inventory-db`
      3. Preview Table `raw_data_442113363817_cdd2b590`
4. Lambda
   1. Configuration -> Environment variables -> Edit
         1. Set `input_bucket` as `raw-data-442113363817-cdd2b590`
   2. Test -> Create new event `TestEvent`
         1. Template `hello-world`
         2. Run test and review logs
```text
Test Event Name
(unsaved) test event

Response
null

Function Logs
START RequestId: 42a85591-5fe4-4a4b-b8a4-52b95ecefd1c Version: $LATEST
Product_id  Product_stock Product_barcode     Product_city  Product_country
0        2862            426        22866882  South Christine             Oman
1        2793            151        47519688    Stevenchester    Liechtenstein
2        8434            904        82958329       Jennyburgh     Saint Martin
3        5094             49        13440886   Bullockchester  Solomon Islands
4        2982             87        02880327       Reyeshaven           Kuwait
END RequestId: 42a85591-5fe4-4a4b-b8a4-52b95ecefd1c
REPORT RequestId: 42a85591-5fe4-4a4b-b8a4-52b95ecefd1c	
Duration: 6225.34 ms	
Billed Duration: 6226 ms	
Memory Size: 128 MB	
Max Memory Used: 128 MB	
Init Duration: 2353.39 ms

Request ID
42a85591-5fe4-4a4b-b8a4-52b95ecefd1c
```

5. Glue
   1. Crawlers
      1. Run crawler `inventory-crawler`
   2. Tables -> `raw_data_442113363817_cdd2b590`
      1. Review table schema versions 0 and 1

## DIY
1. Glue
   1. Tables -> `raw_data_442113363817_cdd2b590` -> Edit schema
      1. Change data type of column `product_id` from `bigint` to `string`
2. Athena
   2. Editor
      1. Data source - AwsDataCatalog
      2. Database - `inventory-db`
      3. Review schema changes in table `raw_data_442113363817_cdd2b590`