# Lab 17. Event-Driven ETL Automation

## Practice
1. S3
   1. Review buckets
      1. `consumption-bucket-332349894090-us-east-1`
      2. `landing-bucket-332349894090-us-east-1`
      3. `staging-bucket-332349894090-us-east-1`
   2. Buckets -> `landing-bucket-332349894090-us-east-1` -> Properties -> Event notifications
      1. Review existing event
         1. Lambda function [start_step_function](start_step_function.py)
         2. Type `All object create events`
2. Glue
   1. Jobs
      2. Go into [JSON2Parquet-job](JSON2Parquet-job.py)
         1. Replace `s3://<Enter-Your-Landing-Bucket-Name>/` on `s3://landing-bucket-332349894090-us-east-1/`
         2. Replace `s3://<Enter-Your-Staging-Bucket-Name>/transformed_data/` on `s3://staging-bucket-332349894090-us-east-1/transformed_data/`
      3. Go into [data-normalization-job](data-normalization-job.py)
         1. Replace `s3://<Enter-Your-Staging-Bucket-Name>/normalized` on `s3://staging-bucket-332349894090-us-east-1/normalized/`
3. Glue
   1. Crawlers -> review two crawlers
      1. `s3_crawler_processed`
      2. `s3_crawler_raw`
4. Step Functions
   1. State machines -> Create state machine
      1. Template `Blank`
      2. Flow -> Design
         1. Add node `Glue: StartJobRun` 
            1. Name `Convert JSON to Parquet`
            2. API Parameters `{ "JobName": "JSON2Parquet-job" }`
            3. Wait for task to complete - selected
         2. Add node `Glue: StartCrawler` 
            1. Name `Create Raw Data Catalog`
            2. API Parameters `{ "Name": "s3_crawler_raw" }`
         3. Add node `Glue: GetCrawler`
            1. Name `Get Status First Crawler`
            2. API Parameters `{ "Name": "s3_crawler_raw" }`
            4. Output
               1. Add original input to output using ResultPath - selected
               2. Combine original input with result `$.response.get_crawler`
         4. Add node `Choice`
            1. Name `Is First Crawler Running?`
            2. Choice rules -> Rule #1 -> Add conditions -> 'OR'
               1. Variable `$.Crawler.State` -> Operator `is equal to` -> Value `String constant` 
               2. `RUNNING` 
               3. OR
               4. Variable `$.Crawler.State` -> Operator `is equal to` -> Value `String constant` 
               5. `STOPPING` 
         5. Add node `Wait` (left branch)
            1. Name `Wait for First Crawler`
            2. Next state `Get Status First Crawler`
         6. Add node `Glue: StartJobRun` (right branch Default)
            1. Name `Process Data`
            2. API Parameters `{ "JobName": "data-normalization-job" }`
            3. Wait for task to complete - selected
         7. Add node `Glue: StartCrawler` (right branch Default)
            1. Name `Create Processed Data Catalog`
            2. API Parameters `{ "JobName": "s3_crawler_processed" }`
         8. Add node `Glue: GetCrawler` (right branch Default)
            1. Name `Get Status Second Crawler`
            2. API Parameters `{ "JobName": "s3_crawler_processed" }`
            3. Output
               1. Add original input to output using ResultPath - selected
               2. Combine original input with result `$.response.get_crawler`
         9. Add node `Choice` (right branch Default)
            1. Name `Is Second Crawler running?`
            2. Choice rules -> Rule #1 -> Add conditions -> 'OR'
               1. Variable `$.response.get_crawler.Crawler.State` -> Operator `is equal to` -> Value `String constant` 
               2. `RUNNING` 
               3. OR
               4. Variable `$.response.get_crawler.Crawler.State` -> Operator `is equal to` -> Value `String constant` 
               5. `STOPPING` 
         10. Add node `Wait` (right branch)
             1. Name `Wait for Second Crawler`
             2. Next state `Get Status Second Crawler`
         11. Add node `Athena StartQueryExecution`
             1. Name `Query Processed Data`
             2. API Parameters: `{ "QueryString": "SELECT SUM(shipping_cost) AS \"Total_Cost_in_$\",SUM(shipping_distance) AS \"Total_Distance_in_miles\", SUM(quantity) AS \"Total_Fuel_Quantity_in_gal\"  FROM \"shipping-db\".\"transformed_data\";",  "WorkGroup": "primary"}`
      3. Flow -> Code
         1. Review [code](state_machine.json)
      4. Flow -> Config
         1. Name `data-workflow`
         2. Type `Standard`
         3. Permissions -> Execution role -> `AWSStepFuntionRole-Lab`
   2. Go into flow `data-workflow`
      1. Copy ARN `arn:aws:states:us-east-1:332349894090:stateMachine:data-workflow`
5. Lambda 
   1. Function `start_step_function` -> Configuration -> Environment variables -> Edit
      1. Set `STATE_MACHINE_ARN` as `arn:aws:states:us-east-1:332349894090:stateMachine:data-workflow` 
   2. Function `shipping_schedule_application` -> Test 
      1. Create new event `testevent`
      2. Template `hello-world`
   3. Run test

```text
Test Event Name
testevent

Response
null

Function Logs
[INFO]	2023-10-18T10:55:01.385Z		Found credentials in environment variables.
START RequestId: aca74847-5d58-4e0b-b45b-570ff571befb Version: $LATEST
[INFO]	2023-10-18T10:55:01.508Z	aca74847-5d58-4e0b-b45b-570ff571befb	event: {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
[INFO]	2023-10-18T10:55:01.508Z	aca74847-5d58-4e0b-b45b-570ff571befb	Generating data
File has been created.
[INFO]	2023-10-18T10:55:01.787Z	aca74847-5d58-4e0b-b45b-570ff571befb	File Uploaded Successfully
[INFO]	2023-10-18T10:55:01.788Z	aca74847-5d58-4e0b-b45b-570ff571befb	empty list
END RequestId: aca74847-5d58-4e0b-b45b-570ff571befb
REPORT RequestId: aca74847-5d58-4e0b-b45b-570ff571befb	Duration: 281.57 ms	Billed Duration: 282 ms	Memory Size: 512 MB	Max Memory Used: 122 MB	Init Duration: 766.04 ms

Request ID
aca74847-5d58-4e0b-b45b-570ff571befb	
```

6. Step Functions
   1. State machines -> `data-workflow`
      1. Executions -> `bdf83bc2-e59b-45ad-9627-02dd3528c2f6`
         1. Review process
7. S3
   1. Bucket `consumption-bucket-332349894090-us-east-1` -> `queries/`
      1. Download [b8117742-43b4-4285-915d-84eadc256a18.csv](b8117742-43b4-4285-915d-84eadc256a18.csv)
8. SNS (Simple Notification Service)
   1. Topics -> `shipping_data_queries` -> Subscriptions -> Create subscription
      1. Protocol -> `Email`
      2. Endpoint -> myemail@gmail.com
9. Confirm subscription

## DIY
1. Step Functions
   1. State machines -> `data-workflow` -> Edit
   2. Add node `SNS Publish` 
      1. Name `Send notification`
      2. Topic `arn:aws:sns:us-east-1:332349894090:shipping_data_queries`
2. Lambda
   2. Function `shipping_schedule_application` -> Test 
      1. Create new event `testevent`
      2. Template `hello-world`
   3. Run test