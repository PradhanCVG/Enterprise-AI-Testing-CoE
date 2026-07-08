/******************************************************************************
 Enterprise AI Testing CoE

 Oracle Database Validation Library

 Database      : Oracle 19c+
 Author        : Enterprise AI Testing CoE
******************************************************************************/

/******************************************************************************
DATABASE INFORMATION
******************************************************************************/

-- Oracle Version
SELECT BANNER
FROM V$VERSION;

-- Database Name
SELECT NAME
FROM V$DATABASE;

-- Database Open Mode
SELECT OPEN_MODE
FROM V$DATABASE;

-- Instance Name
SELECT INSTANCE_NAME
FROM V$INSTANCE;

-- Database Role
SELECT DATABASE_ROLE
FROM V$DATABASE;

-- Startup Time
SELECT STARTUP_TIME
FROM V$INSTANCE;

-- Current User
SELECT USER FROM DUAL;

-- Current Timestamp
SELECT CURRENT_TIMESTAMP FROM DUAL;



/******************************************************************************
SCHEMA VALIDATION
******************************************************************************/

-- Schemas
SELECT USERNAME
FROM ALL_USERS
ORDER BY USERNAME;

-- Tables
SELECT TABLE_NAME
FROM USER_TABLES
ORDER BY TABLE_NAME;

-- Views
SELECT VIEW_NAME
FROM USER_VIEWS;

-- Sequences
SELECT SEQUENCE_NAME
FROM USER_SEQUENCES;

-- Packages
SELECT OBJECT_NAME
FROM USER_OBJECTS
WHERE OBJECT_TYPE='PACKAGE';



/******************************************************************************
OBJECT VALIDATION
******************************************************************************/

SELECT OBJECT_TYPE,
       COUNT(*)
FROM USER_OBJECTS
GROUP BY OBJECT_TYPE
ORDER BY OBJECT_TYPE;

SELECT OBJECT_NAME,
       OBJECT_TYPE
FROM USER_OBJECTS
WHERE STATUS='INVALID';



/******************************************************************************
CONSTRAINT VALIDATION
******************************************************************************/

SELECT *
FROM USER_CONSTRAINTS
WHERE CONSTRAINT_TYPE='P';

SELECT *
FROM USER_CONSTRAINTS
WHERE CONSTRAINT_TYPE='R';

SELECT *
FROM USER_CONSTRAINTS
WHERE CONSTRAINT_TYPE='U';

SELECT *
FROM USER_CONSTRAINTS
WHERE STATUS='DISABLED';



/******************************************************************************
INDEX VALIDATION
******************************************************************************/

SELECT *
FROM USER_INDEXES;

SELECT *
FROM USER_INDEXES
WHERE STATUS='UNUSABLE';

SELECT *
FROM USER_INDEXES
WHERE STATUS<>'VALID';

SELECT *
FROM USER_INDEXES
WHERE UNIQUENESS='UNIQUE';



/******************************************************************************
PARTITION VALIDATION
******************************************************************************/

SELECT *
FROM USER_PART_TABLES;

SELECT *
FROM USER_TAB_PARTITIONS;

SELECT *
FROM USER_PART_INDEXES;

SELECT *
FROM USER_TAB_PARTITIONS
WHERE NUM_ROWS=0;



/******************************************************************************
STATISTICS
******************************************************************************/

SELECT *
FROM USER_TABLES
WHERE LAST_ANALYZED IS NULL;

SELECT *
FROM USER_INDEXES
WHERE LAST_ANALYZED IS NULL;

SELECT *
FROM USER_TAB_STATISTICS
WHERE STALE_STATS='YES';



/******************************************************************************
PERFORMANCE
******************************************************************************/

SELECT SID,
       SERIAL#,
       USERNAME,
       STATUS
FROM V$SESSION;

SELECT *
FROM V$SQLAREA
ORDER BY ELAPSED_TIME DESC
FETCH FIRST 20 ROWS ONLY;

SELECT *
FROM V$SYSTEM_EVENT;

SELECT *
FROM V$SESSION_WAIT;



/******************************************************************************
TABLESPACE
******************************************************************************/

SELECT *
FROM DBA_TABLESPACE_USAGE_METRICS;

SELECT TABLESPACE_NAME,
       STATUS
FROM DBA_TABLESPACES;



/******************************************************************************
DATA QUALITY EXAMPLES
******************************************************************************/

SELECT COUNT(*)
FROM CUSTOMER;

SELECT COUNT(*)
FROM CUSTOMER
WHERE CUSTOMER_ID IS NULL;

SELECT CUSTOMER_ID,
       COUNT(*)
FROM CUSTOMER
GROUP BY CUSTOMER_ID
HAVING COUNT(*)>1;

SELECT *
FROM CUSTOMER
WHERE CREATED_DATE > SYSDATE;



/******************************************************************************
END
******************************************************************************/