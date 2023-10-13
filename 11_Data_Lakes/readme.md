# Lab 11. Data Lakes
> An e-commerce store has a high amount of cart abandonment on a daily basis, and they end up deleting 
> these records from their database to save storage space. 
> The IT manager has asked us to find a cost-effective storage solution to store these records and allow 
> the e-commerce store to perform analytic processing directly on this storage solution.

## Practice
1. S3
   1. Create bucket `consumebucket-lab11`
   2. Create bucket `rawbucket-lab11`
      1. Properties -> Create event notification
         1. Name: `Processor Event`
         2. Type: `PUT`
         3. Destination: `Lambda function` (choose [labFunction-Data-Processor](labFunction-Data-Processor.py))
      2. Properties -> Amazon EventBridge -> Edit -> On
2. Lambda
   1. Function [labFunction-Data-Generator](labFunction-Data-Generator.py)
      1. Configuration -> Environment variables -> Edit
         1. Set `input_bucket` as `rawbucket-lab11`
      2. Test -> Create new event `TestEvent`
         1. Run test and review logs
3. S3
   1. Bucket `rawbucket-lab11`
      1. Download [cart_abandonment_data.csv](cart_abandonment_data.csv)
4. Lambda
   1. Function [labFunction-Data-Processor](labFunction-Data-Processor.py)
      1. Review Target as S3 
      2. Configuration -> Environment variables -> Edit
         1. Set `input_bucket` as `rawbucket-lab11`
         2. Set `output_bucket` as `consumebucket-lab11`
   2. Function [labFunction-Data-Generator](labFunction-Data-Generator.py)
      1. Run test and review logs
5. S3
   1. Bucket `consumebucket-lab11`
      1. Download [cart_aggregated_data.csv](cart_aggregated_data.csv)
6. Amazon EventBridge
   1. Create EventBridge Rule `PromotionApp` with an event pattern
      1. Event source: AWS services
      2. AWS service: S3
      3. Event type: S3 Event Notification -> Object Created -> `rawbucket-lab11`
      4. Select target -> AWS service -> Lambda function -> [labFunction-Promotion-App](labFunction-Promotion-App.py)
7. Lambda
   1. Function [labFunction-Promotion-App](labFunction-Promotion-App.py)
      1. Review Target as EventBridge (CloudWatch Events)
      2. Configuration -> Environment variables -> Edit
         1. Set `input_bucket` as `rawbucket-lab11`
         2. Set `output_bucket` as `consumebucket-lab11`
   2. Function [labFunction-Data-Generator](labFunction-Data-Generator.py)
      1. Run test and review logs
8. S3
   1. Bucket `consumebucket-lab11`
      1. Download [promotion_data.csv](promotion_data.csv)


## DIY
1. Lambda
   1. Function [labFunction-DIY-Processor](labFunction-DIY-Processor.py)
      1. Configuration -> Environment variables -> Edit
         1. Set `input_bucket` as `rawbucket-lab11`
         2. Set `output_bucket` as `consumebucket-lab11`
2. Amazon EventBridge
   1. Create EventBridge Rule `DIYApp` with an event pattern
      1. Event source: AWS services
      2. AWS service: S3
      3. Event type: S3 Event Notification -> Object Created -> `rawbucket-lab11`
      4. Select target -> AWS service -> Lambda function -> [labFunction-DIY-Processor](labFunction-DIY-Processor.py)
3. Lambda
   1. Function [labFunction-DIY-Processor](labFunction-DIY-Processor.py)
         1. Review Target as EventBridge (CloudWatch Events)
   2. Function [labFunction-Data-Generator](labFunction-Data-Generator.py)
         1. Run test and review logs
4. S3
   1. Bucket `consumebucket-lab11`
      1. Download [diy_aggregated_data.csv](diy_aggregated_data.csv)