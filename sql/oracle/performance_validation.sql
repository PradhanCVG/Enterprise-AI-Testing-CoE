/****************************************************************************************
* Oracle Performance Validation
****************************************************************************************/

-- Top SQL by Elapsed Time
SELECT *
FROM (
SELECT
sql_id,
elapsed_time,
executions,
rows_processed
FROM v$sql
ORDER BY elapsed_time DESC
)
WHERE ROWNUM <= 20;

-- Long Running Sessions
SELECT
sid,
serial#,
username,
status,
event
FROM v$session
WHERE status='ACTIVE';