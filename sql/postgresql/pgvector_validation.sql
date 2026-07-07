/****************************************************************************************
* PGVector Validation
****************************************************************************************/

-- Verify pgvector Extension

SELECT *
FROM pg_extension
WHERE extname='vector';

-- Verify Embedding Column

SELECT
table_name,
column_name
FROM information_schema.columns
WHERE udt_name='vector';

-- Missing Embeddings

SELECT *
FROM documents
WHERE embedding IS NULL;

-- Duplicate Documents

SELECT
document_id,
COUNT(*)
FROM documents
GROUP BY document_id
HAVING COUNT(*)>1;

-- Top 5 Similar Documents

SELECT
document_id,
embedding <-> (
SELECT embedding
FROM documents
LIMIT 1
) AS distance
FROM documents
ORDER BY distance
LIMIT 5;