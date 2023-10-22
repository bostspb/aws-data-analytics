# Lab 21. Streaming Ingestion
> A gas station network wants to optimize fuel distribution through the use of analytics. The network would like to 
> send metrics, such as the level of gas stations' fuel tanks, in near real time so that they can automatically ship 
> trucks with additional fuel as the tanks get close to being empty.

## Practice
1. Kinesis Data Firehose
   1. Create delivery stream
      1. Source `Direct PUT`
      2. Destination `Amazon S3`
      3. Name `SI-Firehose`
      4. Transform and convert records -> Enable record format conversion
         1. Output format -> Apache Parquet
         2. AWS Glue region `US East (N. Verginia)`
         3. AWS Glue database `Conversion`
         4. Table -> Browse -> `conversion_table`
      5. Destination settings
         1. S3 bucket `s3://consumption-bucket-332349894090-918`
         2. Dynamic partitioning -> `Enabled`
         3. New line delimiter -> `Enabled`
         4. Inline parsing for JSON -> `Enabled`
         5. Dynamic partitioning keys (Key name: JQ expression)
            1. `station_id`: `.station_id`
            2. `year`: `.event_timestamp| strftime("%Y")`
            3. `month`: `.event_timestamp| strftime("%m")`
            4. `day`: `.event_timestamp| strftime("%d")`
            5. `hour`: `.event_timestamp| strftime("%H")`
         6. S3 bucket prefix `station-data/station_id=` -> Apply dynamic partitioning keys
         7. S3 bucket error output prefix `error`
         8. Retry duration - 60
         9. Buffer hints, compression and encryption -> Buffer interval -> 60
      6. Advanced settings
         1. Service access -> Choose existing IAM role -> `LabStack-*-KinesisFirehoseRole*`
2. Lambda
   1. [GasStationApp](GasStationApp.py)
      1. Configuration -> Environment variables -> Edit
         1. `delivery_stream` -> `SI-Firehose`
      2. Test -> Event name `test` -> Test -> Review log
3. S3
   1. Bucket `consumption-bucket-332349894090-918`
      1. Review folder `station-data/` and subfolders
4. Lambda
   1. [FuelPlanningApp](FuelPlanningApp.py) -> Run Test

```text
Test Event Name
test

Response
[
  "Gas station 9 is low on fuel. Alerting fuel trucks.",
  "Gas station 8 is low on fuel. Alerting fuel trucks.",
  "Gas station 1 is low on fuel. Alerting fuel trucks.",
  "Gas station 2 is low on fuel. Alerting fuel trucks.",
  "Gas station 10 is low on fuel. Alerting fuel trucks.",
  "Gas station 3 is low on fuel. Alerting fuel trucks.",
  "Gas station 4 is low on fuel. Alerting fuel trucks."
]

Function Logs
START RequestId: f19ca3d2-a446-4487-9eda-4611957b9aaa Version: $LATEST
d2a72478-f896-416b-8f40-228e128dce63
875d100e-d333-4a78-b9a0-fa4feeb62f14
0864128e-81d6-43ca-8049-2293f8302279
58456d8f-da05-4c44-9d55-038e834f4b79
4986d2b5-5907-4a19-9fc7-8d2c1adcabac
496ec58a-47f2-4448-936e-d74fac99eb56
9be4b793-69d9-40b6-b8ff-57da272d3c51
END RequestId: f19ca3d2-a446-4487-9eda-4611957b9aaa
REPORT RequestId: f19ca3d2-a446-4487-9eda-4611957b9aaa	Duration: 6613.76 ms	Billed Duration: 6614 ms	Memory Size: 128 MB	Max Memory Used: 71 MB	Init Duration: 259.75 ms

Request ID
f19ca3d2-a446-4487-9eda-4611957b9aaa
```

5. SQS
   1. Queues -> `Fuel_Planning_Queue` -> Review Messages available - 7
6. Lambda
   1. [FuelTruckApp](FuelTruckApp.py) -> Run Test

```text
Test Event Name
test

Response
"Messages processed: 1"

Function Logs
START RequestId: 055b2d2d-2973-43e7-8f5c-be81be7ec5aa Version: $LATEST
Fuel truck has been dispatched to gas station 10.
END RequestId: 055b2d2d-2973-43e7-8f5c-be81be7ec5aa
REPORT RequestId: 055b2d2d-2973-43e7-8f5c-be81be7ec5aa	Duration: 1506.60 ms	Billed Duration: 1507 ms	Memory Size: 128 MB	Max Memory Used: 69 MB	Init Duration: 267.51 ms

Request ID
055b2d2d-2973-43e7-8f5c-be81be7ec5aa
```
...
```text
...
Response
"Messages processed: 1"
...
```
...
```text
Test Event Name
test

Response
"No messages found in queue. Messages processed: 0"

Function Logs
START RequestId: 20eb813f-5e45-4220-8863-5bbada96f474 Version: $LATEST
END RequestId: 20eb813f-5e45-4220-8863-5bbada96f474
REPORT RequestId: 20eb813f-5e45-4220-8863-5bbada96f474	Duration: 5193.19 ms	Billed Duration: 5194 ms	Memory Size: 128 MB	Max Memory Used: 70 MB

Request ID
20eb813f-5e45-4220-8863-5bbada96f474
```

7. SQS
   1. Queues -> `Fuel_Planning_Queue` -> Review Messages available - 0


## DIY
1. Kinesis
   1. Data Firehose -> `SI-Firehose` -> Configuration -> Destination settings -> Edit
      1. Dynamic partitioning keys -> Add 
         1. `minute`: `.event_timestamp| strftime("%M")`
      2. Apply dynamic partitioning keys