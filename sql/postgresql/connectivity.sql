/****************************************************************************************
* File Name   : connectivity.sql
* Description : PostgreSQL Connectivity Validation
****************************************************************************************/

SELECT version();

SELECT current_database();

SELECT current_user;

SELECT current_schema();

SELECT now() AS current_timestamp;

SHOW server_version;

SHOW timezone;

SELECT inet_server_addr(),
       inet_server_port();

SELECT pg_postmaster_start_time();