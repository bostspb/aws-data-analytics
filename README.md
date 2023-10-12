# AWS Cloud Quest: Data Analytics
> ID: E-0JMPNM <br>
> https://explore.skillbuilder.aws/learn/course/15601/aws-cloud-quest-data-analytics <br>

`AWS` `S3` `EC2` `Lambda` `RDS` `IAM` `DynamoDB` `Athena` `Glue` `Kinesis` `OpenSearch` `EMR`
`Apache Spark` `Lake Formation`

As the city’s AWS Data Analytics specialist, you will gain hands-on experience with scalable data lakes, 
data warehousing, real-time data ingestion, big data analytics, log analytics, streaming analytics, data storage, 
and business intelligence dashboards.


### 1. Cloud Computing Essentials :heavy_check_mark:
The city's web portal needs to migrate the beach wave size prediction page to AWS to improve reliability. 	
- Articulate the characteristics of the AWS cloud computing platform.
- Describe the core benefits of using AWS products and services.
- Compare and contrast AWS cloud services to On-Premises infrastructure.
- Implement hosting a static web page using Amazon S3.

### 2. Cloud First Steps :heavy_check_mark:
The island's stabilization system is failing and needs increased reliability and availability for its computational modules. 	
- Summarize AWS Infrastructure benefits.
- Describe AWS Regions and Availability Zones.
- Deploy Amazon EC2 instances into multiple Availability Zones.

### 3. Serverless Foundations :heavy_check_mark:
Help the Amusement Park IT Department to run code without provisioning a server. 	
- Describe the principles of serverless computing
- Describe AWS Lambda and detail its uses and benefits
- Create and deploy an AWS Lambda function

### 4. Computing Solutions :heavy_check_mark:
The school server that runs the scheduling solution needs more memory. Assist with vertically scaling their Amazon EC2 instance. 	
- Describe Amazon EC2 instance families and instance types.
- Describe horizontal and vertical scaling.
- Recognize options for connecting to Amazon EC2 instances.

### 5. Networking Concepts :heavy_check_mark:
Help the bank setup a secure networking environment which allows communication between resources and the internet. 	
- Define key features of VPCs, subnets, internet gateways and route tables.
- Describe the benefits of using Amazon VPCs.
- State the basics of CIDR block notation and IP addressing.
- Explain how VPC traffic is routed and secured using gateways, network access control lists, and security groups.

### 6. Databases in Practice :heavy_check_mark:
Improve the insurance company's relational database operations, performance, and availability. 	
- Review the features, benefits and database types available with Amazon RDS.
- Describe vertical and horizontal scaling on Amazon RDS.
- Use Amazon RDS read replicas to increase database performance.
- Implement multi-AZ deployments of Amazon RDS to increase availability.

### 7. Core Security Concepts :heavy_check_mark:
Help improve security at the city's stock exchange by ensuring that support engineers can only perform authorized actions. 	
- Describe the creation process and differences between AWS IAM users, roles, and groups.
- Review the structure and components of AWS IAM Policies.
- Summarize the AWS Shared Responsibility Model and compliance programs.

### 8. First NoSQL Database 	
Help the island's streaming entertainment service implement a NoSQL database to develop new features. 	
- Set Up a NoSQL database with Amazon DynamoDB. 
- Interact with the elements and attributes of an Amazon DynamoDB database. 
- Describe the features and benefits of Amazon DynamoDB. 
- Summarize the different uses of common purpose-built databases.

### 9. Data Ingestion Methods :heavy_check_mark: 	
Help the package delivery company speed up data ingestion and transformation. 	
- Configure data pre-processing using AWS Lambda. 
- Create an Amazon Kinesis Data Analytics application. 
- Create an Amazon Kinesis Data Firehose delivery stream. 
- Send real-time analytics to an Amazon DynamoDB table. 
- Configure real-time analytics of data in your application.

[Practice & DIY](09_Data_Ingestion_Methods/readme.md)

### 10. Design NoSQL Databases 	
Help Felipe, the Island Gamers CTO to improve the performance of the top players scoreboard. 	
- Understand how to design an efficient Amazon DynamoDB table based on access patterns
- Comprehend performance differences between Amazon DynamoDB scan and query
- Configure Amazon DynamoDB global secondary index to improve search performance
- Write Python code to query or scan Amazon DynamoDB tables using global secondary indexes

### 11. Data Lakes 	 
An e-commerce store has a high amount of cart abandonment on a daily basis, and they end up deleting these records 
from their database to save storage space. The IT manager has asked us to find a cost-effective storage solution to 
store these records and allow the e-commerce store to perform analytic processing directly on this storage solution. 
- Describe the components of a data lake.
- Describe how to organize your data into layers (or zones) in Amazon S3. 
- Explain how to use Amazon S3 as the storage layer of your data lake. 
- Describe the value of data lakes. 

### 12. Querying the Data Lake
A financial institution has recently implemented a data lake to ingest transactions from all across the city. 
A credit card issuer has begun to send logs of transactions which are being stored in Amazon S3. 
The financial institution's fraud department would like to start analyzing the logs for suspicious transactions and 
would like a fast and scalable solution to achieve this.
- Explain how to query Amazon Athena tables for suspicious credit card transactions. 
- Explain how Amazon Athena can ingest data from files. 
- Define how to save the results of Amazon Athena queries to Amazon S3. 
- Demonstrate how AWS Lambda can be used to generate test data for testing.

### 13. Federated Queries 
City hall has developed a ticketing system to manage citizen requests. Tickets include cases such as notifications 
of street damage, burned out streetlights, and even noisy establishments. Now, to plan better, city hall wants to 
use SQL to obtain more insights from these requests, such as the most common problem areas.
- Explain how to use an AWS Glue crawler to expose Amazon DynamoDB tables to a data lake. 
- Identify how to use Amazon Athena Federated Query to directly query DynamoDB by using a scalable SQL engine.

### 14. Cloud Data Warehouse 	
A game studio captures player data from its most successful games. The studio wants to analyze the data to 
increase revenue from in-game purchases. 	
- Explain how to Implement a data warehouse in Amazon Redshift. 
- Describe how to use an AWS Glue built-in transformation to flatten semi-structured data containing nested data and array structures.

### 15. Streaming Ingestion
A gas station network wants to optimize fuel distribution through the use of analytics. The network would like to 
send metrics, such as the level of gas stations' fuel tanks, in near real time so that they can automatically ship 
trucks with additional fuel as the tanks get close to being empty. 	
- Use Amazon Kinesis Data Firehose to ingest data directly to your data lake. 
- Call Amazon Athena to query data in near real time using a Python SDK. 

### 16. Documents Indexing and Search 	 
The bank would like to increase the number of online transactions customers can review from 6 months to five years. 
In addition, the online bank statements must support textual searches for all fields in the statement. 	 
- Define how to use AWS OpenSearch to index and search documents Explain how to use AWS Glue Jobs to ingest data 
into Amazon OpenSearch Service Explain how to consume data from OpenSearch Service using a restful API

### 17. Distributed Large-Scale Data Processing 	
Our city taxi service collects and stores large amounts of data. We’d like to use that data to improve our service 
and be more efficient. We want to use Amazon EMR, with Apache Spark, to process the data stored in Amazon S3. 
After the data is processed, our analysts can use Amazon Athena to query it with the help of AWS Glue. 	
- Explain how to use a Jupyter notebook to process a large dataset. 
- Demonstrate how to create an Amazon EMR cluster. 
- Define how to query the AWS Glue table using Amazon Athena. 
- Describe how to write data to an AWS Glue table using Apache Spark.

### 18. Securing the Data Lake
A bank with several departments is using a data lake powered by Amazon S3. They need your help implementing 
security rules that limit access to sensitive data within its table’s metadata catalog. 
- Define how to query data as different IAM users to test the restrictions. 
- Explain how an AWS Glue crawler ingests data from files located in an Amazon S3 bucket. 
- Describe how, using Lake Formation, to restrict access to sensitive data for certain IAM users. 
- Define how to use AWS Lake Formation to configure access to the data for AWS IAM users.

### 19. Real Time Data Processing
The city administration wants to improve the efficiency of its wind farm. When a wind generator in the wind farm 
fails, it takes a long time to identify the fault, send a maintenance team, and carry out the repair.
The administration wants to anticipate possible defects in the wind turbines in order to provide preventive maintenance. 	
- Explain how to create Amazon Kinesis Data Analytics application code using SQL to process incoming streaming data. 
- Explain how to use Amazon Kinesis Data Analytics to write application output records to a configured destination. 
- Define how to deploy Amazon Kinesis Data Streams to ingest data from streaming data sources. 
