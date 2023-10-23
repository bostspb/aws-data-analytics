# Lab 22. Real Time Data Processing
> The city administration wants to improve the efficiency of its wind farm. When a wind generator in the wind farm 
> fails, it takes a long time to identify the fault, send a maintenance team, and carry out the repair.
> The administration wants to anticipate possible defects in the wind turbines in order to provide preventive maintenance.

## Practice
1. S3
   1. Bucket `kinesis-flink-application-20fbeb00`
      1. `AnomalyDetection.jar`
      2. `MaxWindSpeed.jar`
2. EC2
   1. Instances -> `Wind Turbine Simulator`
      1. Open Public IPv4 address -> `http://44.207.171.92/kinesis`
3. Kinesis
   1. Kinesis Data Streams -> Create data stream
      1. Name `WindDataStream`
      2. Capacity mode `Provisioned`
4. `http://44.207.171.92/kinesis`
   1. Amazon Kinesis data stream name `WindDataStream` -> Submit -> Start
5. Kinesis
   1. Data streams 
      1. `WindDataStream` -> Data viewer -> Shard -> Choose one -> Latest -> Get records -> Review list of records
      2. Create data stream
         1. Name `AnomalyDetectionStream`
         2. Capacity mode `Provisioned`
      3. Managed Apache Flink 
6. Managed Apache Flink
   1. Streaming applications -> Create streaming application
      1. Create from scratch
      2. Name `AnomalyDetection`
      3. Access to application resources -> Choose from IAM roles -> `lab-kinesis-analytics-role`
      4. Templates -> `Development`
   2. `AnomalyDetection`
      1. Configure
         1. Application code location
            1. Amazon S3 bucket -> `s3://kinesis-flink-application-20fbeb00`
            2. Path to S3 object `AnomalyDetection.jar` ([RandomCutForest](https://github.com/aws-samples/amazon-kinesis-data-analytics-examples/tree/master/AnomalyDetection/RandomCutForest))
            3. Access to application resources -> Choose from IAM roles -> `lab-kinesis-analytics-role`
         2. Runtime properties
            1. Add -> `lab` : `inputStreamName` : `WindDataStream`
            2. Add -> `lab` : `outputStreamName` : `AnomalyDetectionStream`
            3. Add -> `lab` : `region` : `us-east-1`
      2. Run -> Run with latest snapshot -> Run
7. `http://44.207.171.92/kinesis`
   1. `Wind speed data set` -> Start
8. Kinesis
   1. Data streams 
      1. `AnomalyDetection` -> Data viewer -> Shard -> Choose one -> Latest -> Get records -> Review list of records
9. `http://44.207.171.92/kinesis`
   1. `Wind speed anomaly data set` -> Start
10. Lambda
    1. Function [AnalyticsDestinationFunction](AnalyticsDestinationFunction.py)
       1. Add trigger -> Source `Kinesis`
          1. Kinesis stream `AnomalyDetectionStream`
          2. Activate trigger -> Selected
11. DynamoDB
    1. Tables -> Explore items -> `WindDataTable` -> Review items
12. SNS
    1. Topics -> `AnomalyNotification` -> Create subscription via Email
13. Lambda
    1. Function [AnomalyMessageDeliveryFunction](AnomalyMessageDeliveryFunction.py)
    2. Test -> `AnomalyNotification` -> Save -> Test
    3. Review received three emails


## DIY
1. Managed Apache Flink
   1. Streaming applications -> Create streaming application
      1. Create from scratch
      2. Name `CalculateMaxSpeed`
      3. Access to application resources -> Choose from IAM roles -> `lab-kinesis-analytics-role`
      4. Templates -> `Development`
   2. `CalculateMaxSpeed`
      1. Configure
         1. Application code location
            1. Amazon S3 bucket -> `s3://kinesis-flink-application-20fbeb00`
            2. Path to S3 object `MaxWindSpeed.jar`
            3. Access to application resources -> Choose from IAM roles -> `lab-kinesis-analytics-role`
      2. Run -> Run with latest snapshot -> Run
2. Kinesis
   1. Kinesis Data Streams -> Create data stream
      1. Name `MaxWindSpeed`
      2. Capacity mode `Provisioned`
3. Lambda
    1. Function [DIYFunction](DIYFunction.py)
       1. Add trigger -> Source `Kinesis`
          1. Kinesis stream `MaxWindSpeed`
          2. Activate trigger -> Selected
4. DynamoDB
    1. Tables -> Explore items -> `DIYTable` -> Review items