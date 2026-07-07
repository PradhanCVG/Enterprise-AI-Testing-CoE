/****************************************************************************************
* PostgreSQL Constraint Validation
****************************************************************************************/

SELECT
conname,
contype,
conrelid::regclass
FROM pg_constraint
ORDER BY conrelid;