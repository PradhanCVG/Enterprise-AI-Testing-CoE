/****************************************************************************************
* PostgreSQL Schema Validation
****************************************************************************************/

-- List Schemas
SELECT schema_name
FROM information_schema.schemata
ORDER BY schema_name;

-- List Tables
SELECT table_schema,
       table_name
FROM information_schema.tables
WHERE table_type='BASE TABLE'
ORDER BY table_schema, table_name;

-- List Views
SELECT table_schema,
       table_name
FROM information_schema.views
ORDER BY table_schema, table_name;

-- List Functions
SELECT routine_schema,
       routine_name
FROM information_schema.routines
ORDER BY routine_schema, routine_name;