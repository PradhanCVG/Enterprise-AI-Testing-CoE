/******************************************************************************
 Enterprise AI Testing CoE

 ETL Validation SQL Library

 Supported Databases
 - Oracle
 - PostgreSQL
******************************************************************************/

/******************************************************************************
SOURCE VALIDATION
******************************************************************************/

-- Source Record Count
SELECT COUNT(*)
FROM CUSTOMER;

-- Source NULL Customer IDs
SELECT COUNT(*)
FROM CUSTOMER
WHERE CUSTOMER_ID IS NULL;

-- Source Duplicate Customer IDs
SELECT CUSTOMER_ID,
       COUNT(*)
FROM CUSTOMER
GROUP BY CUSTOMER_ID
HAVING COUNT(*) > 1;

-- Source Maximum Created Date
SELECT MAX(CREATED_DATE)
FROM CUSTOMER;


/******************************************************************************
TARGET VALIDATION
******************************************************************************/

-- Target Record Count
SELECT COUNT(*)
FROM customer;

-- Target NULL Customer IDs
SELECT COUNT(*)
FROM customer
WHERE customer_id IS NULL;

-- Target Duplicate Customer IDs
SELECT customer_id,
       COUNT(*)
FROM customer
GROUP BY customer_id
HAVING COUNT(*) > 1;

-- Target Maximum Created Date
SELECT MAX(created_date)
FROM customer;


/******************************************************************************
SOURCE TO TARGET RECONCILIATION
******************************************************************************/

-- Compare Record Counts
SELECT COUNT(*)
FROM CUSTOMER;

SELECT COUNT(*)
FROM customer;

-- Compare Distinct Customer IDs
SELECT COUNT(DISTINCT CUSTOMER_ID)
FROM CUSTOMER;

SELECT COUNT(DISTINCT customer_id)
FROM customer;


/******************************************************************************
DATA QUALITY
******************************************************************************/

-- NULL Validation
SELECT COUNT(*)
FROM customer
WHERE email IS NULL;

-- Blank Customer Name
SELECT COUNT(*)
FROM customer
WHERE TRIM(customer_name) = '';

-- Invalid Status
SELECT *
FROM customer
WHERE status NOT IN ('ACTIVE', 'INACTIVE');

-- Future Dates
SELECT *
FROM customer
WHERE created_date > CURRENT_TIMESTAMP;


/******************************************************************************
INCREMENTAL LOAD
******************************************************************************/

-- Today's Records
SELECT COUNT(*)
FROM customer
WHERE created_date::date = CURRENT_DATE;

-- Latest Load Timestamp
SELECT MAX(created_date)
FROM customer;


/******************************************************************************
BATCH VALIDATION
******************************************************************************/

-- Latest Batch
SELECT MAX(batchid)
FROM batchstatistics;

-- Successful Batches
SELECT *
FROM batchstatistics
WHERE status = 'SUCCESS';

-- Failed Batches
SELECT *
FROM batchstatistics
WHERE status = 'FAILED';

-- Batch Duration
SELECT batchid,
       starttime,
       endtime
FROM batchstatistics;


/******************************************************************************
TRANSFORMATION VALIDATION
******************************************************************************/

-- Uppercase Customer Name
SELECT *
FROM customer
WHERE customer_name <> UPPER(customer_name);

-- Invalid Email
SELECT *
FROM customer
WHERE email IS NULL;

-- Duplicate Email
SELECT email,
       COUNT(*)
FROM customer
GROUP BY email
HAVING COUNT(*) > 1;


/******************************************************************************
FILE VALIDATION (Reference)
******************************************************************************/

-- Expected File Columns

-- CUSTOMER_ID
-- CUSTOMER_NAME
-- EMAIL
-- STATUS
-- CREATED_DATE

/******************************************************************************
END
******************************************************************************/