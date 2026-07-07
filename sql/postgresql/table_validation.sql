/****************************************************************************************
* PostgreSQL Table Validation
****************************************************************************************/

-- Table Sizes

SELECT
schemaname,
tablename,
pg_size_pretty(pg_total_relation_size(schemaname||'.'||tablename)) AS size
FROM pg_tables
ORDER BY pg_total_relation_size(schemaname||'.'||tablename) DESC;

-- Estimated Row Count

SELECT
relname,
n_live_tup
FROM pg_stat_user_tables
ORDER BY n_live_tup DESC;

-- Dead Tuples

SELECT
relname,
n_dead_tup
FROM pg_stat_user_tables
ORDER BY n_dead_tup DESC;