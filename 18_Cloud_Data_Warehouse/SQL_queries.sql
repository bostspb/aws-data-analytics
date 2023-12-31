-- Step 43: Retrieve data from the players_data table and sort by game_details

SELECT * FROM "games-flattened-data-db"."players_data"
ORDER BY game_details;


-- Step 45: Retrieve data from the games_data table and sort by id and index

SELECT * FROM "games-flattened-data-db"."games_data"
ORDER BY id, index;


-- Step 52: Create external schema in Amazon Redshift

create EXTERNAL SCHEMA players_schema
FROM DATA CATALOG
database 'games-flattened-data-db'
IAM_ROLE 'ENTER YOUR IAM ROLE ARN ASSOCIATED WITH AMAZON REDSHIFT'
create EXTERNAL DATABASE if not exists;


-- Step 54: Retrieve data from the players_data table and sort by game_details

SELECT * FROM players_schema.players_data
ORDER BY game_details;


-- Step 56: Retrieve data from the games_data table and sort by id and index

SELECT * FROM players_schema.games_data
ORDER BY id, index;


-- Step 58: Find the purchases by the player with ID 12345

SELECT g.id as Id, p.name as Name, g.purchased_item as Purchased_item, '$'||g.purchases as Purchases
FROM players_schema.players_data p, players_schema.games_data g
WHERE p.game_details = g.id AND g.id='12345'; 


-- Step 60: Create a materialized view

DROP MATERIALIZED VIEW IF EXISTS mv_players_purchases;
CREATE MATERIALIZED VIEW mv_players_purchases AS (
SELECT g.id as Id, p.name as Name, g.purchased_item as Purchased_item, '$'||g.purchases as Purchases
FROM players_schema.players_data p, players_schema.games_data g
WHERE p.game_details = g.id); 


-- Step 62: Find the purchases by the player with ID 12345 using a materialized view

SELECT * FROM mv_players_purchases
WHERE id='12345';

--
-- DIY: Hints
-- 1. Use the following name for your materialized view:
--
-- mv_players_purchases_amount
--
-- 2. Create the materialized view based on the following query:
--
SELECT g.id as Id, p.name as Name, '$'||SUM(g.purchases) as Total_Purchases
FROM players_schema.players_data p, players_schema.games_data g
WHERE p.game_details = g.id 
GROUP BY g.id, p.name