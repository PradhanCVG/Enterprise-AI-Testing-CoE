/****************************************************************************************
* PostgreSQL Performance Validation
****************************************************************************************/

-- Long Running Queries

SELECT
pid,
query,
state,
query_start
FROM pg_stat_activity
WHERE state='active';

-- Missing Index Usage

SELECT
relname,
seq_scan,
idx_scan
FROM pg_stat_user_tables
ORDER BY seq_scan DESC;

-- Slow Queries

SELECT *
FROM pg_stat_statements
ORDER BY total_exec_time DESC
LIMIT 20;