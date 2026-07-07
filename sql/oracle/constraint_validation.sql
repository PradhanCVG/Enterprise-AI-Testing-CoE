/****************************************************************************************
* Constraint Validation
****************************************************************************************/

-- Primary Keys
SELECT owner,
       table_name,
       constraint_name
FROM all_constraints
WHERE constraint_type='P';

-- Foreign Keys
SELECT owner,
       table_name,
       constraint_name
FROM all_constraints
WHERE constraint_type='R';

-- Unique Constraints
SELECT owner,
       table_name,
       constraint_name
FROM all_constraints
WHERE constraint_type='U';

-- Check Constraints
SELECT owner,
       table_name,
       constraint_name
FROM all_constraints
WHERE constraint_type='C';