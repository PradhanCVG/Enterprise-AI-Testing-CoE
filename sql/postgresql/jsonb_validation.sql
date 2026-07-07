/****************************************************************************************
* JSONB Validation
****************************************************************************************/

-- NULL JSON

SELECT *
FROM documents
WHERE metadata IS NULL;

-- Empty JSON

SELECT *
FROM documents
WHERE metadata='{}';

-- Missing Attribute

SELECT *
FROM documents
WHERE NOT(metadata ? 'document_type');

-- Missing Language

SELECT *
FROM documents
WHERE NOT(metadata ? 'language');

-- Invalid Metadata

SELECT *
FROM documents
WHERE jsonb_typeof(metadata)<>'object';