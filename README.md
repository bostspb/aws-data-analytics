# AWS Cloud Quest: Data Analytics
> ID: E-0JMPNM <br>
> https://explore.skillbuilder.aws/learn/course/15601/aws-cloud-quest-data-analytics <br>
> Certificate https://www.credly.com/badges/f7405252-e9a3-42fc-ac3e-7676727fe639/public_url

`AWS` `S3` `EC2` `Lambda` `RDS` `IAM` `VPC` `DynamoDB` `Athena` `Glue` `Kinesis` `OpenSearch` `EMR`
`Apache Spark` `Lake Formation` `Cloud9` `CloudFormation`

As the city’s AWS Data Analytics specialist, you will gain hands-on experience with scalable data lakes, 
data warehousing, real-time data ingestion, big data analytics, log analytics, streaming analytics, data storage, 
and business intelligence dashboards.


### 1. Cloud Computing Essentials :heavy_check_mark:
`Amazon S3` 

The city's web portal needs to migrate the beach wave size prediction page to AWS to improve reliability. 	
- Articulate the characteristics of the AWS cloud computing platform.
- Describe the core benefits of using AWS products and services.
- Compare and contrast AWS cloud services to On-Premises infrastructure.
- Implement hosting a static web page using Amazon S3.


### 2. Cloud First Steps :heavy_check_mark:
`Amazon EC2` 

The island's stabilization system is failing and needs increased reliability and availability for its computational modules. 	
- Summarize AWS Infrastructure benefits.
- Describe AWS Regions and Availability Zones.
- Deploy Amazon EC2 instances into multiple Availability Zones.


### 3. Serverless Foundations :heavy_check_mark:
`AWS Lambda`

Help the Amusement Park IT Department to run code without provisioning a server. 	
- Describe the principles of serverless computing
- Describe AWS Lambda and detail its uses and benefits
- Create and deploy an AWS Lambda function


### 4. Computing Solutions :heavy_check_mark:
`Amazon EC2` 

The school server that runs the scheduling solution needs more memory. Assist with vertically scaling their Amazon EC2 instance. 	
- Describe Amazon EC2 instance families and instance types.
- Describe horizontal and vertical scaling.
- Recognize options for connecting to Amazon EC2 instances.


### 5. Networking Concepts :heavy_check_mark:
`Amazon EC2` `Amazon VPC`

Help the bank setup a secure networking environment which allows communication between resources and the internet. 	
- Define key features of VPCs, subnets, internet gateways and route tables.
- Describe the benefits of using Amazon VPCs.
- State the basics of CIDR block notation and IP addressing.
- Explain how VPC traffic is routed and secured using gateways, network access control lists, and security groups.

[Plan](05_Networking_Concepts/05_Networking_Concepts.jpg)


### 6. Databases in Practice :heavy_check_mark:
`Amazon RDS`

Improve the insurance company's relational database operations, performance, and availability. 	
- Review the features, benefits and database types available with Amazon RDS.
- Describe vertical and horizontal scaling on Amazon RDS.
- Use Amazon RDS read replicas to increase database performance.
- Implement multi-AZ deployments of Amazon RDS to increase availability.


### 7. Core Security Concepts :heavy_check_mark:
`AWS IAM` `Amazon EC2` `Amazon RDS`

Help improve security at the city's stock exchange by ensuring that support engineers can only perform authorized actions. 	
- Describe the creation process and differences between AWS IAM users, roles, and groups.
- Review the structure and components of AWS IAM Policies.
- Summarize the AWS Shared Responsibility Model and compliance programs.


### 8. First NoSQL Database :heavy_check_mark:
`Amazon DynamoDB`

Help the island's streaming entertainment service implement a NoSQL database to develop new features. 	
- Set Up a NoSQL database with Amazon DynamoDB. 
- Interact with the elements and attributes of an Amazon DynamoDB database. 
- Describe the features and benefits of Amazon DynamoDB. 
- Summarize the different uses of common purpose-built databases.

[Plan](08_First_NoSQL_Database/08_First_NoSQL_Database.jpg)


### 9. Data Ingestion Methods :heavy_check_mark: 	
`Kinesis` `Lambda` `DynamoDB` `AWS Glue` `Athena` `S3` `EC2`

Help the package delivery company speed up data ingestion and transformation. 	
- Configure data pre-processing using AWS Lambda. 
- Create an Amazon Kinesis Data Analytics application. 
- Create an Amazon Kinesis Data Firehose delivery stream. 
- Send real-time analytics to an Amazon DynamoDB table. 
- Configure real-time analytics of data in your application.

 [Plan](09_Data_Ingestion_Methods/09_Data_Ingestion_Methods.jpg), [Practice & DIY](09_Data_Ingestion_Methods/readme.md)


### 10. Design NoSQL Databases 	:heavy_check_mark:
`Amazon DynamoDB` `AWS Lambda` `AWS Cloud9`

Help Felipe, the Island Gamers CTO to improve the performance of the top players scoreboard. 	
- Understand how to design an efficient Amazon DynamoDB table based on access patterns
- Comprehend performance differences between Amazon DynamoDB scan and query
- Configure Amazon DynamoDB global secondary index to improve search performance
- Write Python code to query or scan Amazon DynamoDB tables using global secondary indexes

[Plan](10_Design_NoSQL_Databases/10_Design_NoSQL_Databases.jpg), [Tests](10_Design_NoSQL_Databases/dynamoDB-tests)


### 11. Data Lakes  :heavy_check_mark:
`AWS Lambda` `Amazon S3` `Amazon EventBridge`

An e-commerce store has a high amount of cart abandonment on a daily basis, and they end up deleting these records 
from their database to save storage space. The IT manager has asked us to find a cost-effective storage solution to 
store these records and allow the e-commerce store to perform analytic processing directly on this storage solution. 
- Describe the components of a data lake.
- Describe how to organize your data into layers (or zones) in Amazon S3. 
- Explain how to use Amazon S3 as the storage layer of your data lake. 
- Describe the value of data lakes. 

[Plan](11_Data_Lakes/11_Data_Lakes.jpg), [Practice & DIY](11_Data_Lakes/readme.md)


### 12. Querying the Data Lake  :heavy_check_mark:
`AWS Lambda` `Amazon Athena` `Amazon S3`

A financial institution has recently implemented a data lake to ingest transactions from all across the city. 
A credit card issuer has begun to send logs of transactions which are being stored in Amazon S3. 
The financial institution's fraud department would like to start analyzing the logs for suspicious transactions and 
would like a fast and scalable solution to achieve this.
- Explain how to query Amazon Athena tables for suspicious credit card transactions. 
- Explain how Amazon Athena can ingest data from files. 
- Define how to save the results of Amazon Athena queries to Amazon S3. 
- Demonstrate how AWS Lambda can be used to generate test data for testing.

[Plan](12_Querying_the_Data_Lake/12_Querying_the_Data_Lake.jpg), [Practice & DIY](12_Querying_the_Data_Lake/readme.md)


### 13. Federated Queries  :heavy_check_mark: 
`Amazon Athena` `Amazon S3` `AWS Glue` `Amazon DynamoDB`

City hall has developed a ticketing system to manage citizen requests. Tickets include cases such as notifications 
of street damage, burned out streetlights, and even noisy establishments. Now, to plan better, city hall wants to 
use SQL to obtain more insights from these requests, such as the most common problem areas.
- Explain how to use an AWS Glue crawler to expose Amazon DynamoDB tables to a data lake. 
- Identify how to use Amazon Athena Federated Query to directly query DynamoDB by using a scalable SQL engine.

[Plan](13_Federated_Queries/13_Federated_Queries.jpg), [Practice & DIY](13_Federated_Queries/readme.md)


### 14. Populating Data Catalog  :heavy_check_mark: 
`Amazon Athena` `Amazon S3` `AWS Glue` `AWS Lambda` 

Help to better organize data lake. 
- Create a database in the AWS Glue Data Cataloge.
- Create and run AWS Glue crawler in the Data Catalog.
- Use Amazon Athena to query data in the table.
- Rerun the crawler to update the Data Catalog.

[Plan](14_Populating_Data_Catalog/14_Populating_Data_Catalog.jpg), [Practice & DIY](14_Populating_Data_Catalog/readme.md)


### 15. Event-Driven Serverless ETL  :heavy_check_mark: 
`AWS Glue`, `Amazon Redshift`, `Amazon 53`

The management of an electronic toll collection company wants to consolidate the billing of the toll plazas 
in the data warehouse with the most up-to-date data. 
- Recognize how to create an AWS Glue connection to Amazon Redshift. 
- Explore the use of AWS Glue crawlers. 
- Determine how create an ETL job in AWS Glue Studio to move data from an Amazon S3 bucket to Amazon Redshift. 
- Define how to create an AWS Glue workflow to automate the data processing pipeline. 
- Demonstrate how to use Amazon 53 Event Notifications and AWS Lambda to start the workflow. 
- Demonstrate how to query the data using the Amazon Redshift query editor.

[Plan](15_Event_Driven_Serverless_ETL/15_Event_Driven_Serverless_ETL.jpg), [Practice & DIY](15_Event_Driven_Serverless_ETL/readme.md)


### 16. Securing the Data Lake  :heavy_check_mark: 
`CloudFormation` `S3` `AWS Lake Formation` `Athena`

A bank with several departments is using a data lake powered by Amazon S3. They need your help implementing 
security rules that limit access to sensitive data within its table’s metadata catalog. 
- Define how to query data as different IAM users to test the restrictions. 
- Explain how an AWS Glue crawler ingests data from files located in an Amazon S3 bucket. 
- Describe how, using Lake Formation, to restrict access to sensitive data for certain IAM users. 
- Define how to use AWS Lake Formation to configure access to the data for AWS IAM users.

[Plan](16_Securing_the_Data_Lake/16_Securing_the_Data_Lake.jpg), [Practice & DIY](16_Securing_the_Data_Lake/readme.md)


### 17. Event-Driven ETL Automation  :heavy_check_mark: 
`AWS Glue` `AWS Lambda` `AWS Step Functions` `Amazon Athena` `Amazon 53`

A logistics company wants to plan the purchase of fuel for its trucks based on the amount of cargo to be 
transported and the distance the trucks will travel. The company wants a daily report that contains aggregated 
information about the next day's deliveries, and it wants the process to be automated through a workflow. 
- Determine how to configure a data analytics workflow to process shipping data by using Workflow 
  Studio for AWS Step Functions. 
- Examine the servertess orchestration of extract, transform, and load (ETL) pipelines. 

[Plan](17_Event_Driven_ETL_Automation/17_Event_Driven_ETL_Automation.jpg), [Practice & DIY](17_Event_Driven_ETL_Automation/readme.md)


### 18. Cloud Data Warehouse  :heavy_check_mark: 
`AWS Glue` `Amazon Redshift` `Amazon Athena` `Amazon Kinesis`

A game studio captures player data from its most successful games. The studio wants to analyze the data to 
increase revenue from in-game purchases. 	
- Explain how to Implement a data warehouse in Amazon Redshift. 
- Describe how to use an AWS Glue built-in transformation to flatten semi-structured data containing nested data and array structures.

[Plan](18_Cloud_Data_Warehouse/18_Cloud_Data_Warehouse.jpg), [Practice & DIY](18_Cloud_Data_Warehouse/readme.md)


### 19. Documents Indexing and Search  :heavy_check_mark: 
`AWS Glue` `Amazon OpenSearch Service` `Amazon S3`

The bank would like to increase the number of online transactions customers can review from 6 months to five years. 
In addition, the online bank statements must support textual searches for all fields in the statement. 	 
- Define how to use AWS OpenSearch to index and search documents Explain how to use AWS Glue Jobs to ingest data 
into Amazon OpenSearch Service Explain how to consume data from OpenSearch Service using a restful API

[Plan](19_Documents_Indexing_and_Search/19_Documents_Indexing_and_Search.jpg), [Practice & DIY](19_Documents_Indexing_and_Search/readme.md)


### 20. Daily Batch Extraction  :heavy_check_mark:
`Amazon RDS` `AWS Glue` `Amazon S3` `Amazon Athena` `AWS Secrets Manager`

- Determine how to create JDBC connections in AWS Glue that will connect databases to ingest, transform 
  and extract data.
- Determine how to use AWS Glue Studio to visually create Spark scripts to extract, transform, and ingest data 
  from a variety of different sources and destinations.
- Demonstrate how to use Amazon Athena to run on-demand queries on the data extracted by AWS Glue. 

[Plan](20_Daily_Batch_Extraction/20_Daily_Batch_Extraction.jpg), [Practice & DIY](20_Daily_Batch_Extraction/readme.md)


### 21. Streaming Ingestion  :heavy_check_mark:
`Amazon SQS` `AWS Lambda` `Amazon Kinesis` `Amazon S3` `Amazon Athena`

A gas station network wants to optimize fuel distribution through the use of analytics. The network would like to 
send metrics, such as the level of gas stations' fuel tanks, in near real time so that they can automatically ship 
trucks with additional fuel as the tanks get close to being empty. 	
- Use Amazon Kinesis Data Firehose to ingest data directly to your data lake. 
- Call Amazon Athena to query data in near real time using a Python SDK. 

[Plan](21_Streaming_Ingestion/21_Streaming_Ingestion.jpg), [Practice & DIY](21_Streaming_Ingestion/readme.md)


### 22. Real Time Data Processing  :heavy_check_mark:
`Amazon Kinesis` `AWS Lambda` `Amazon DynamoDB` `Amazon SNS` `Amazon S3`

The city administration wants to improve the efficiency of its wind farm. When a wind generator in the wind farm 
fails, it takes a long time to identify the fault, send a maintenance team, and carry out the repair.
The administration wants to anticipate possible defects in the wind turbines in order to provide preventive maintenance. 	
- Explain how to create Amazon Kinesis Data Analytics application code using SQL to process incoming streaming data. 
- Explain how to use Amazon Kinesis Data Analytics to write application output records to a configured destination. 
- Define how to deploy Amazon Kinesis Data Streams to ingest data from streaming data sources. 

[Plan](22_Real_Time_Data_Processing/22_Real_Time_Data_Processing.jpg), [Practice & DIY](22_Real_Time_Data_Processing/readme.md)
