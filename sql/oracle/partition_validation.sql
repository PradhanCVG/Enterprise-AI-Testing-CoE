/****************************************************************************************
* Oracle Partition Validation
****************************************************************************************/

-- Partitioned Tables
SELECT owner,
       table_name,
       partitioning_type
FROM all_part_tables;

-- Partition Details
SELECT
table_owner,
table_name,
partition_name,
high_value
FROM all_tab_partitions;

-- Interval Partitioned Tables
SELECT
owner,
table_name,
interval
FROM all_part_tables
WHERE interval='YES';