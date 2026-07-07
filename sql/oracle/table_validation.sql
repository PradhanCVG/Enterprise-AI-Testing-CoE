/****************************************************************************************
* File Name   : table_validation.sql
* Description : Oracle Table Validation
****************************************************************************************/

PROMPT ==========================================================
PROMPT Table Validation
PROMPT ==========================================================

-- Table Row Counts
SELECT owner,
       table_name,
       num_rows
FROM all_tables
ORDER BY owner, table_name;

-- Empty Tables
SELECT owner,
       table_name
FROM all_tables
WHERE num_rows = 0;

-- Table Size (MB)
SELECT
owner,
segment_name,
ROUND(bytes/1024/1024,2) SIZE_MB
FROM dba_segments
WHERE segment_type='TABLE'
ORDER BY SIZE_MB DESC;