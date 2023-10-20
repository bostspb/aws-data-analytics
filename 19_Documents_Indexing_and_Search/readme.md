# Lab 19. Documents Indexing and Search
> The bank would like to increase the number of online transactions customers can review from 6 months to five years. 
> In addition, the online bank statements must support textual searches for all fields in the statement. 	

## Practice
1. OpenSearch Service
   1. Dashboard -> Create domain
      1. Name `bank-transactions`
      2. Domain creation method `Standard`
      3. Templates `Dev/test`
      4. Deployment option(s)
         1. Domain without standby
         2. Availability Zone(s) `2-AZ`
      5. Engine options -> Version -> Elasticsearch 7.10
      6. Instance type `m5.large.search`
      7. Nodes - 2
      8. Network `Public access`
      9. Fine-grained access control
         1. Enable fine-grained access control - Selected
         2. Create master user: `lab-user`, `LabUserP433!`
      10. Access policy -> Only use fine-grained access control
2. S3
   1. Bucket `ingestion-bucket-332349894090-us-east-1`
      1. Copy S3 URI of file `elasticsearch-hadoop-7.8.0.jar` -> `s3://ingestion-bucket-332349894090-us-east-1/elasticsearch-hadoop-7.8.0.jar`
      2. Copy S3 URI of folder `input/` -> `s3://ingestion-bucket-332349894090-us-east-1/input/`
      3. Folder `input/`
         1. Review object `transactions.csv.gz`
3. Glue
   1. ETL jobs -> Create job -> Script Editor
      1. Engine `Spark (Python)`
      2. Upload file [glue_to_opensearch_job.py](glue_to_opensearch_job.py)
      3. Job details
         1. Name `bank-transactions-ingestion-job`
         2. IAM role `AWSGlueServiceRole-lab`
         3. Glue version `Glue 2.0 - Supports spark 2.4, Scala 2, Python 3`
         4. Job bookmark `Disable`
         5. Number of retries - 0
         6. Advanced properties -> Libraries -> Dependent JARs path -> `s3://ingestion-bucket-332349894090-us-east-1/elasticsearch-hadoop-7.8.0.jar`
4. OpenSearch Service
   1. Dashboard -> Domain `bank-transactions`
      1. Copy Domain endpoint - `https://search-bank-transactions-43quunikiejd7lpit6z7nst6wi.us-east-1.es.amazonaws.com`
5. Glue
   1. ETL jobs -> `bank-transactions-ingestion-job` -> Job details
      1. Advanced properties -> Job parameters
         1. Add param `--es_endpoint` with value `https://search-bank-transactions-43quunikiejd7lpit6z7nst6wi.us-east-1.es.amazonaws.com`
         2. Add param `--es_user` with value `lab-user`
         3. Add param `--es_pass` with value `LabUserP433!`
         4. Add param `--input_bucket` with value `s3://ingestion-bucket-332349894090-us-east-1/input/`
      2. Save & Run
6. EC2
   1. Instances -> `SearchInstance` -> Copy Public IPv4 address
      1. Open Search web-app in browser
         1. Search terms like "cash", "credit", "debit"
7. OpenSearch Service 
   1. Dashboard -> Domain `bank-transactions`
      1. Open Kibana URL
         1. Enter with creds `lab-user`, `LabUserP433!`
         2. Open on my own -> Select your tenant -> Private
         3. Interact with the Elasticsearch API
         4. Send default request and then others requests:

```text
# This query searches all indexes in your cluster.
GET _search
{
  "query": {
    "match_all": {}
  }
}
```

```text
GET /main-index/_search
{
  "query": {
    "match_all": {}
  }
}
```

```text
GET /main-index/_search
{
   "query" : {
       "query_string" :  { 
           "query": "debit",
           "fields":  ["type"]
        }
    }
}
```

```text
GET /main-index/_search
{
   "query" : {
       "query_string" :  { 
           "query": "credit",
           "fields":  ["type"]
        }
    }
}
```


## DIY
1. Glue
   1. ETL jobs -> `bank-transactions-ingestion-job`
      1. Change target column `balance` to `account_balance`
      2. Change target column `amount` to `transaction_amount`
      3. Remove column `k_symbol`
      4. Change index name `main-index/transactions` to `new-index/transactions`
      5. Save & Run

[New version](glue_to_opensearch_job_v2.py) of `glue_to_opensearch_job.py`