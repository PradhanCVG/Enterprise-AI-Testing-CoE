-- Sample SQL queries for database test validation

SELECT current_database() AS database_name;

SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'public';

SELECT column_name, data_type
FROM information_schema.columns
WHERE table_name = 'example_table';
