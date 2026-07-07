/****************************************************************************************
* AI Readiness Validation
* Validate data before AI ingestion
****************************************************************************************/

-- NULL Text
SELECT COUNT(*)
FROM documents
WHERE document_text IS NULL;

-- Empty Text
SELECT COUNT(*)
FROM documents
WHERE LENGTH(TRIM(document_text)) = 0;

-- Duplicate Documents
SELECT document_id,
COUNT(*)
FROM documents
GROUP BY document_id
HAVING COUNT(*) > 1;

-- Missing Metadata
SELECT *
FROM documents
WHERE document_type IS NULL
OR language IS NULL;

-- Large Documents (>100 KB)
SELECT
document_id,
LENGTH(document_text)
FROM documents
WHERE LENGTH(document_text) > 100000;