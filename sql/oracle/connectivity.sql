/****************************************************************************************
* File Name   : connectivity.sql
* Description : Oracle Database Connectivity Validation
* Purpose     : Verify database availability and connection details before ETL/AI testing
****************************************************************************************/

PROMPT ==========================================================
PROMPT Oracle Database Connectivity Validation
PROMPT ==========================================================

-- Database Version
SELECT * FROM v$version;

-- Current Database Name
SELECT name FROM v$database;

-- Instance Information
SELECT
    instance_name,
    host_name,
    version,
    status,
    startup_time
FROM v$instance;

-- Current User
SELECT USER FROM dual;

-- Current Schema
SELECT SYS_CONTEXT('USERENV','CURRENT_SCHEMA') AS CURRENT_SCHEMA
FROM dual;

-- Current Timestamp
SELECT SYSTIMESTAMP FROM dual;

-- Database Time Zone
SELECT dbtimezone FROM dual;

-- Session Time Zone
SELECT sessiontimezone FROM dual;

-- Verify Read/Write Mode
SELECT open_mode FROM v$database;

PROMPT Connectivity Validation Completed.