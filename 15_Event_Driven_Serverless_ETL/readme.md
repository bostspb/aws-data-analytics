# Lab 15. Event-Driven Serverless ETL

## Practice
1. S3 
   1. Bucket `landing-bucket-332349894090-us-east-1` -> Properties -> Create event notification
      1. Name `s3Event`
      2. Suffix `.json`
      3. Type `Put`
      4. Destination - Lambda function [start_workflow_function](start_workflow_function.py)
2. Redshift
   1. Clusters -> `toll-cluster-332349894090-us-east-1`
   2. Copy JDBC URL `jdbc:redshift://toll-cluster-332349894090-us-east-1.cm4cw2akqoyb.us-east-1.redshift.amazonaws.com:5439/toll_db`
   3. Query in query editor
      1. Connect to database 
         1. Connection - Create a new connection
         2. Authentication - Temporary credentials
         3. Cluster `toll-cluster-442113363817-us-east-1`
         4. Database `toll_db`
         5. User `admin`
      2. Run query on `toll_db.public`:

```sql
CREATE TABLE toll_table (
  transaction_id bigint,
  transaction_date character varying NOT null,
  toll_booth character varying NOT null,
  vehicle_make character varying NOT null,
  vehicle_category character varying NOT null,
  transaction_amount REAL
);
```

3. Secrets Manager
   1. Secrets -> `tollclusterSecret3FAE9071-pIsCgB3UhsEC` -> Retrieve secret value

```json
{
	"dbClusterIdentifier": "toll-cluster-332349894090-us-east-1",
	"password": "Iud`,}2NKj%c8,IUa1f_i0x=1<mrlU",
	"dbname": "toll_db",
	"engine": "redshift",
	"port": 5439,
	"host": "toll-cluster-332349894090-us-east-1.cm4cw2akqoyb.us-east-1.redshift.amazonaws.com",
	"username": "admin"
}
```

4. VPC
   1. Your VPCs
      1. Copy VPC ID of `LabVPC` - `vpc-01febc42154bbb3e7`
   2. Subnets
      1. Copy Subnet ID of subnet wit name like `*/database-*` - `subnet-0e80fbea0b9c7d139`
5. Glue
   1. Data connections -> Create connection
      1. Name `redshift_conn`
      2. Type `JDBC`
      3. JDBC URL `jdbc:redshift://toll-cluster-332349894090-us-east-1.cm4cw2akqoyb.us-east-1.redshift.amazonaws.com:5439/toll_db`
      4. Username `admin`
      5. Password "Iud`,}2NKj%c8,IUa1f_i0x=1<mrlU"
      6. VPC `vpc-01febc42154bbb3e7`
      7. Subnet `subnet-0e80fbea0b9c7d139`
      8. Security groups `Redshift Security Group`
   2. Crawlers
      1. Review crawler `s3_crawler` (it adds a Data Catalog for JSON data in an S3 bucket)
      2. Create crawler `Redshift-Crawler`
         1. Add a data source
            1. Data source `JDBC`
            2. Connection `redshift_conn`
            3. Include path `toll_db/public/%`
         2. IAM role `AWSGlueServiceRole-Lab`
         3. Target database `toll-raw-db`
      3. Run crawler `Redshift-Crawler`
   3. Data catalog -> Tables
      1. Review table `landing_bucket_332349894090_us_east_1`
      2. Review table `toll_db_public_toll_table`
   4. ETL jobs
      1. Visual with a blank canvas -> Create
         1. Add node from Sources tab -> `S3`
            1. S3 source type `Data Catalog table`
            2. Database `toll_raw_db`
            3. Table `landing_bucket_332349894090_us_east_1`
         2. Add node from Transforms tab -> Change Schema
            1. Change Schema (Apply mapping) 
               1. `transaction_id` -> `bigint`
         3. Add node from Targets tab -> Redshift
            1. Redshift access type `Glue Data Catalog tables`
            2. Database `toll_raw_db`
            3. Table `toll_db_public_toll_table`
            4. Performance and security -> S3 staging directory -> `s3://staging-bucket-332349894090-us-east-1`
         4. Job details
            1. Name `s3_to_redshift_job`
            2. IAM role `AWSGlueServiceRole-Lab`
            3. Requested number of workers - 3
            4. Number of retries - 1
            5. Job timeout (minutes) - 15
            6. Advanced properties -> Job metrics -> unselect
   5. Data Integration and ETL -> Workflows
      1. Review `Lab-Workflow` (it runs the `s3_crawler` to create a table)       
      2. Add workflow
         1. Name `redshift_workflow`
         2. Max concurrency - 2
      3. Workflow `redshift_workflow`
         1. Add new "On demand" trigger `redshift-workflows-start`
         2. Graph 
            1. Add node -> Crawlers -> `s3_crawler`
            2. Crawler `s3_crawler` -> Add trigger `s3-crawler-event`
               1. Trigger type `Event`
               2. Trigger logic `Start after ANY watched event`
            3. Add node -> Jobs -> `s3_to_redshift_job`
6. Lambda
   1. Toll_Plaza_Application
      1. Test -> Config test event -> Create new `TestEvent`
      2. Run test

```text
Test Event Name
TestEvent

Response
null

Function Logs
[INFO]	2023-10-17T08:38:30.971Z		Found credentials in environment variables.
START RequestId: 11ec5b3e-9043-4a24-ab6c-97c431c05f86 Version: $LATEST
[INFO]	2023-10-17T08:38:31.109Z	11ec5b3e-9043-4a24-ab6c-97c431c05f86	event: {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
[INFO]	2023-10-17T08:38:31.109Z	11ec5b3e-9043-4a24-ab6c-97c431c05f86	Error: 'RequestType'
[INFO]	2023-10-17T08:38:31.110Z	11ec5b3e-9043-4a24-ab6c-97c431c05f86	Generating data
File has been created.
[INFO]	2023-10-17T08:38:31.519Z	11ec5b3e-9043-4a24-ab6c-97c431c05f86	File Uploaded Successfully
[INFO]	2023-10-17T08:38:31.519Z	11ec5b3e-9043-4a24-ab6c-97c431c05f86	empty list
[INFO]	2023-10-17T08:38:31.519Z	11ec5b3e-9043-4a24-ab6c-97c431c05f86	Upload Complete
END RequestId: 11ec5b3e-9043-4a24-ab6c-97c431c05f86
REPORT RequestId: 11ec5b3e-9043-4a24-ab6c-97c431c05f86	Duration: 411.77 ms	Billed Duration: 412 ms	Memory Size: 512 MB	Max Memory Used: 159 MB	Init Duration: 1300.90 ms

Request ID
11ec5b3e-9043-4a24-ab6c-97c431c05f86
```

7. Redshift
   1. Query editor
      1. Connect to database
      2. Preview data of table `toll_table`


## DIY
1. Glue
   1. ETL jobs -> `s3_to_redshift_job` -> Job details 
      1. Job metrics -> Select
2. Lambda
   1. Toll_Plaza_Application
      2. Run test

```text
Test Event Name
TestEvent

Response
null

Function Logs
[INFO]	2023-10-17T09:06:18.873Z		Found credentials in environment variables.
START RequestId: a9c06112-b91f-4069-a0ca-f80aabb65a4a Version: $LATEST
[INFO]	2023-10-17T09:06:19.013Z	a9c06112-b91f-4069-a0ca-f80aabb65a4a	event: {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
[INFO]	2023-10-17T09:06:19.013Z	a9c06112-b91f-4069-a0ca-f80aabb65a4a	Error: 'RequestType'
[INFO]	2023-10-17T09:06:19.013Z	a9c06112-b91f-4069-a0ca-f80aabb65a4a	Generating data
File has been created.
[INFO]	2023-10-17T09:06:19.475Z	a9c06112-b91f-4069-a0ca-f80aabb65a4a	File Uploaded Successfully
[INFO]	2023-10-17T09:06:19.475Z	a9c06112-b91f-4069-a0ca-f80aabb65a4a	empty list
[INFO]	2023-10-17T09:06:19.475Z	a9c06112-b91f-4069-a0ca-f80aabb65a4a	Upload Complete
END RequestId: a9c06112-b91f-4069-a0ca-f80aabb65a4a
REPORT RequestId: a9c06112-b91f-4069-a0ca-f80aabb65a4a	Duration: 464.46 ms	Billed Duration: 465 ms	Memory Size: 512 MB	Max Memory Used: 159 MB	Init Duration: 1324.93 ms

Request ID
a9c06112-b91f-4069-a0ca-f80aabb65a4a
```