--Query1

CREATE TABLE AwsDataCatalog.glue_ticket_db.requests
WITH (
        external_location = 's3://<DATA_LAKE_BUCKET_NAME>/requests'
        )
AS SELECT *
FROM "glue-etl-ticket-table";



--Query2

SELECT RequestType, COUNT(* )
FROM "requests"   
GROUP BY RequestType
Order by 2 DESC;


--Query3

SELECT RequestType, COUNT(*)
FROM "athena-federated-dynamodb"."default"."dynamodbtickettable"  
GROUP BY RequestType
Order by 2 DESC;

