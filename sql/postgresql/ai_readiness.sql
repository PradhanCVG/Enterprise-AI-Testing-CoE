/****************************************************************************************
* AI Readiness Validation
****************************************************************************************/

-- NULL Documents

SELECT COUNT(*)
FROM documents
WHERE content IS NULL;

-- Empty Documents

SELECT COUNT(*)
FROM documents
WHERE length(trim(content))=0;

-- Duplicate Document IDs

SELECT
document_id,
COUNT(*)
FROM documents
GROUP BY document_id
HAVING COUNT(*)>1;

-- Missing Metadata

SELECT *
FROM documents
WHERE metadata IS NULL;

-- Missing Embeddings

SELECT *
FROM documents
WHERE embedding IS NULL;

-- Oversized Documents

SELECT
document_id,
length(content)
FROM documents
WHERE length(content)>100000;