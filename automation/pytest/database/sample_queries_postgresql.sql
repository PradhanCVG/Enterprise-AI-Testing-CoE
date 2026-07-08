/******************************************************************************
 Enterprise AI Testing CoE

 PostgreSQL Validation Library

 Database : PostgreSQL 14+
******************************************************************************/

/******************************************************************************
DATABASE INFORMATION
******************************************************************************/

-- PostgreSQL Version
SELECT version();

-- Database Name
SELECT current_database();

-- Current User
SELECT current_user;

-- Current Timestamp
SELECT CURRENT_TIMESTAMP;

-- Server Start Time
SELECT pg_postmaster_start_time();

-- Database Size
SELECT pg_size_pretty(pg_database_size(current_database()));



/******************************************************************************
SCHEMA VALIDATION
******************************************************************************/

SELECT schema_name
FROM information_schema.schemata
ORDER BY schema_name;

SELECT table_name
FROM information_schema.tables
WHERE table_schema='public';

SELECT table_name
FROM information_schema.views
WHERE table_schema='public';

SELECT sequence_name
FROM information_schema.sequences;



/******************************************************************************
OBJECT VALIDATION
******************************************************************************/

SELECT table_schema,
       table_name
FROM information_schema.tables
ORDER BY table_name;



/******************************************************************************
CONSTRAINT VALIDATION
******************************************************************************/

SELECT constraint_name,
       constraint_type
FROM information_schema.table_constraints;

SELECT *
FROM information_schema.referential_constraints;

SELECT *
FROM information_schema.key_column_usage;



/******************************************************************************
INDEX VALIDATION
******************************************************************************/

SELECT *
FROM pg_indexes;

SELECT *
FROM pg_stat_user_indexes;

SELECT *
FROM pg_index;



/******************************************************************************
PARTITION VALIDATION
******************************************************************************/

SELECT *
FROM pg_partitioned_table;

SELECT *
FROM pg_inherits;

SELECT relname
FROM pg_class
WHERE relkind='p';



/******************************************************************************
STATISTICS
******************************************************************************/

SELECT *
FROM pg_stat_user_tables;

SELECT *
FROM pg_stat_user_indexes;

SELECT *
FROM pg_stat_database;



/******************************************************************************
PERFORMANCE
******************************************************************************/

SELECT *
FROM pg_stat_activity;

SELECT *
FROM pg_locks;

SELECT *
FROM pg_stat_statements
ORDER BY total_exec_time DESC
LIMIT 20;



/******************************************************************************
STORAGE
******************************************************************************/

SELECT pg_size_pretty(pg_database_size(current_database()));

SELECT schemaname,
       tablename,
       pg_size_pretty(pg_total_relation_size(tablename))
FROM pg_tables
WHERE schemaname='public';



/******************************************************************************
DATA QUALITY EXAMPLES
******************************************************************************/

SELECT COUNT(*)
FROM customer;

SELECT COUNT(*)
FROM customer
WHERE customer_id IS NULL;

SELECT customer_id,
       COUNT(*)
FROM customer
GROUP BY customer_id
HAVING COUNT(*)>1;

SELECT *
FROM customer
WHERE created_date > CURRENT_DATE;



/******************************************************************************
EXTENSIONS
******************************************************************************/

SELECT *
FROM pg_extension;



/******************************************************************************
ACTIVE CONNECTIONS
******************************************************************************/

SELECT pid,
       usename,
       application_name,
       state,
       query
FROM pg_stat_activity;



/******************************************************************************
END
******************************************************************************/