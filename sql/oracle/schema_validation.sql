/****************************************************************************************
* File Name   : schema_validation.sql
* Description : Oracle Schema Validation
****************************************************************************************/

PROMPT ==========================================================
PROMPT Oracle Schema Validation
PROMPT ==========================================================

-- List Schemas
SELECT username
FROM dba_users
ORDER BY username;

-- List Tables
SELECT owner,
       table_name
FROM all_tables
ORDER BY owner, table_name;

-- List Views
SELECT owner,
       view_name
FROM all_views
ORDER BY owner, view_name;

-- List Materialized Views
SELECT owner,
       mview_name
FROM all_mviews
ORDER BY owner, mview_name;

-- List Packages
SELECT owner,
       object_name
FROM all_objects
WHERE object_type='PACKAGE'
ORDER BY owner, object_name;

-- List Procedures
SELECT owner,
       object_name
FROM all_objects
WHERE object_type='PROCEDURE'
ORDER BY owner, object_name;

-- List Functions
SELECT owner,
       object_name
FROM all_objects
WHERE object_type='FUNCTION'
ORDER BY owner, object_name;

-- Invalid Objects
SELECT owner,
       object_name,
       object_type
FROM all_objects
WHERE status='INVALID'
ORDER BY owner;