# Lab 16. Securing the Data Lake
> A bank with several departments is using a data lake powered by Amazon S3. They need your help implementing 
> security rules that limit access to sensitive data within its table’s metadata catalog.


## Practice
1. CloudFormation
   1. Stacks -> `LabStack-*-0` -> Outputs
   2. Copy LoginURL `https://332349894090.signin.aws.amazon.com/console`
2. S3
   1. Bucket `operations-datalake-332349894090-us-east-1` -> `input/` 
      1. `customer/` -> [customerData.csv](customerData.csv)
      2. `employee/` -> [employeeData.csv](employeeData.csv)
3. Glue
   1. Data Catalog -> Crawlers
      1. Create crawler `OpsIngestionCrawler`
         1. Add a data source
               1. Data source `S3`
               2. S3 path `s3://operations-datalake-332349894090-us-east-1`
               3. Subsequent crawler runs - Crawl all sub-folders
         2. Existing IAM role `OpsIngestionCrawlerRole`
         3. Target database -> Add database -> `ops_data_ingestion`
         4. Crawler schedule -> Frequency -> On demand
      2. Run crawler `OpsIngestionCrawler`
   2. Data Catalog -> Tables -> `operations_datalake_332349894090_us_east_1`
      1. Review Columns:
         - employee_id
         - social_security
         - checking_account
         - routing_number
4. Lake Formation
   1. Welcome to Lake Formation -> Add myself -> Get started
   2. Tables -> `operations_datalake_332349894090_us_east_1` -> Actions -> Grant
      1. Principals -> IAM users and roles -> `OpsUser`
      2. LF-Tags or catalog resources -> Named Data Catalog resources
         1. Databases -> `ops_data_ingestion`
         2. Tables -> `operations_datalake_332349894090_us_east_1`
         3. Data filters -> Create new
            1. Name `ops_filter`
            2. Column-level access -> Exclude columns
               - employee_id
               - social_security
               - checking_account
               - routing_number
            3. Row filter expression -> `true`
         4. Data filter permissions -> `select`
         5. Grantable permissions-> `select`
   3. Permissions -> Grant
      1. Principals -> IAM users and roles -> `opsDirector`
      2. LF-Tags or catalog resources -> Named Data Catalog resources
         1. Databases -> `ops_data_ingestion`
         2. Tables -> `operations_datalake_332349894090_us_east_1`
      3. Table permissions -> `select`
      4. Data permissions -> `All data access`
   4. Permissions -> `IAMAllowedPrincipals` (with Resource type `Database`) -> Revoke
   5. Permissions -> `IAMAllowedPrincipals` (with Resource type `Table`) -> Revoke
5. Sing out -> go to URL `https://332349894090.signin.aws.amazon.com/console` -> sing in as `OpsUser`
6. Athena
   1. Query editor -> Preview table `ops_data_ingestion.operations_datalake_332349894090_us_east_1`
      1. Review columns - there aren't `employee_id`, `social_security`, `checking_account` and `routing_number`
7. Sing out -> go to URL `https://332349894090.signin.aws.amazon.com/console` -> sing in as `opsDirector`
8. Athena
   1. Query editor -> Preview table `ops_data_ingestion.operations_datalake_332349894090_us_east_1`
      1. Review columns - all columns are displayed
9. Sing out 


## DIY
1. Lake Formation
   1. Permissions -> Grant
      1. Principals -> IAM users and roles -> `opsManager`
      2. LF-Tags or catalog resources -> Named Data Catalog resources
         1. Databases -> `ops_data_ingestion`
         2. Tables -> `operations_datalake_332349894090_us_east_1`
      3. Table permissions -> `select`
      4. Data permissions -> `All data access`