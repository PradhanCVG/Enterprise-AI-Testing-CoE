/****************************************************************************************
* PostgreSQL Security Validation
****************************************************************************************/

-- Roles

SELECT rolname
FROM pg_roles;

-- Users

SELECT usename
FROM pg_user;

-- Database Privileges

SELECT *
FROM information_schema.role_table_grants;

-- Row Level Security

SELECT
tablename,
rowsecurity
FROM pg_tables;