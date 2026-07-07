/****************************************************************************************
* Oracle Security Validation
****************************************************************************************/

-- Users
SELECT username,
account_status
FROM dba_users;

-- Roles
SELECT *
FROM dba_roles;

-- System Privileges
SELECT *
FROM dba_sys_privs;

-- Object Privileges
SELECT *
FROM dba_tab_privs;