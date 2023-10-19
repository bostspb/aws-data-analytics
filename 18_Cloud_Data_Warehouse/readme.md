# Lab 18. Cloud Data Warehouse
> A game studio captures player data from its most successful games. 
> The studio wants to analyze the data to increase revenue from in-game purchases. 

## Practice
1. S3
   1. Review bucket `athena-results-332349894090-440`
   2. Review bucket `consumption-data-332349894090-440`
   3. Review bucket `raw-data-332349894090-440` -> `players_gamesData.json` (257.9 MB)
2. Glue
   1. Databases
      1. Review `games-data-db`
      2. Review `games-flattened-data-db`
   2. Tables
      1. Review `games-data-db.raw_data_332349894090_440` (with location `s3://raw-data-332349894090-440/`)
         1. Schema -> column `game_details` (array):
```json
{
  "game_details": [
    {
      "game_name": "string",
      "high_score": "int",
      "purchased_item": "string",
      "purchases": "int"
    }
  ]
}
```

3. Athena
   1. Query editor -> Preview table `games-data-db.raw_data_332349894090_440`
      1. Results -> Preferences -> Wrap lines
4. Glue
   1. ETL jobs -> Create job (Script Editor) -> Spark (Python)
      1. Replace code on [AWS_Glue_job_script](AWS_Glue_job_script.py)
      2. Replace `YOUR AWS GLUE RAW DATA TABLE NAME` on `raw_data_332349894090_440`
      3. Replace `YOUR CONSUMPTION DATA S3 BUCKET NAME` on `raw-data-332349894090-440`
      4. Replace `YOUR CONSUMPTION DATA S3 BUCKET NAME` on `consumption-data-332349894090-440`
      5. Job details
         1. Name `games-flattened-data-job`
         2. IAM role `aws_glue_role`
      6. Save & Run
   2. Crawlers -> Create crawler 
      1. Name `games-flattened-data-crawler`
      2. Add data source -> S3 -> `s3://consumption-data-332349894090-440/parquet/`
      3. IAM role `aws_glue_role`
      4. Target database `games-flattened-data-db`
   3. Crawlers -> Run crawler `games-flattened-data-crawler`
   4. Tables
      1. Review new tables and them schemas
         1. `games-flattened-data-db.games_data`
         2. `games-flattened-data-db.players_data`
5. Athena
   1. Query editor -> Run queries from file [SQL_queries.sql](SQL_queries.sql)
      1. `SELECT * FROM "games-flattened-data-db"."players_data" ORDER BY game_details;`
      2. `SELECT * FROM "games-flattened-data-db"."games_data" ORDER BY id, index;`
6. Redshift
   1. Clusters -> `games-db-cluster-332349894090-us-east-1` -> Actions -> Manage IAM roles
      1. Copy role ARN `arn:aws:iam::332349894090:role/LabStack-d5e806f7-8d16-4d-redshiftspectrumroleE0198-WoY23BMRR3oz`
   2. Query editor -> Connect to database
         1. Create new connection
         2. Temporary credentials
         3. Cluster `games-db-cluster-332349894090-us-east-1`
         4. Database `games_rs_db`
         5. Table `awsuser`
   3. Query editor -> Run queries from file [SQL_queries.sql](SQL_queries.sql)

```sql
-- Step 52: Create external schema in Amazon Redshift
create EXTERNAL SCHEMA players_schema
FROM DATA CATALOG
database 'games-flattened-data-db'
IAM_ROLE 'arn:aws:iam::332349894090:role/LabStack-d5e806f7-8d16-4d-redshiftspectrumroleE0198-WoY23BMRR3oz'
create EXTERNAL DATABASE if not exists;
```

```sql
-- Step 54: Retrieve data from the players_data table and sort by game_details
SELECT * FROM players_schema.players_data
ORDER BY game_details;
```

```sql
-- Step 56: Retrieve data from the games_data table and sort by id and index
SELECT * FROM players_schema.games_data
ORDER BY id, index;
```

```sql
-- Step 58: Find the purchases by the player with ID 12345
SELECT g.id as Id, p.name as Name, g.purchased_item as Purchased_item, '$'||g.purchases as Purchases
FROM players_schema.players_data p, players_schema.games_data g
WHERE p.game_details = g.id AND g.id='12345'; 

-- ELAPSED TIME: 00 m 08 s

-- id,name,purchased_item,purchases
-- 12345,Daniel Mccoy,drinks,$4
-- 12345,Daniel Mccoy,clothes,$84
```

```sql
-- Step 60: Create a materialized view
DROP MATERIALIZED VIEW IF EXISTS mv_players_purchases;
CREATE MATERIALIZED VIEW mv_players_purchases AS (
SELECT g.id as Id, p.name as Name, g.purchased_item as Purchased_item, '$'||g.purchases as Purchases
FROM players_schema.players_data p, players_schema.games_data g
WHERE p.game_details = g.id); 
```

```sql
-- Step 62: Find the purchases by the player with ID 12345 using a materialized view
SELECT * FROM mv_players_purchases
WHERE id='12345';

-- ELAPSED TIME: 00 m 02 s

-- id,name,purchased_item,purchases
-- 12345,Daniel Mccoy,drinks,$4
-- 12345,Daniel Mccoy,clothes,$84
```

## DIY
6. Redshift
   1. Query editor -> Run queries

```sql
SELECT g.id as Id, p.name as Name, '$'||sum(g.purchases)
FROM players_schema.players_data p
LEFT JOIN players_schema.games_data g ON p.game_details = g.id
WHERE g.id='12345'
GROUP BY g.id, p.name

-- ELAPSED TIME: 00 m 07 s

-- id,name,column
-- 12345,Daniel Mccoy,$88
```

```sql
DROP MATERIALIZED VIEW IF EXISTS mv_players_purchases_amount;
CREATE MATERIALIZED VIEW mv_players_purchases_amount AS (
   SELECT g.id as Id, p.name as Name, '$'||SUM(g.purchases) as Total_Purchases
   FROM players_schema.players_data p, players_schema.games_data g
   WHERE p.game_details = g.id 
   GROUP BY g.id, p.name
)
```

```sql
SELECT Id, Name, Total_Purchases
FROM mv_players_purchases_amount
where Id = '12345'

-- ELAPSED TIME: 00 m 02 s

-- id,name,total_purchases
-- 12345,Daniel Mccoy,$88
```