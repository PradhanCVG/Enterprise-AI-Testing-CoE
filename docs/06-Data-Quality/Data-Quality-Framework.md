# Data Quality Framework

> *Data quality is the foundation of trustworthy AI. Every AI response is only as reliable as the data used to generate it.*

---

# Purpose

This document defines the Enterprise Data Quality Framework for validating structured, semi-structured, and unstructured data before it is consumed by AI applications.

The framework establishes standardized data quality dimensions, validation techniques, automation strategies, quality metrics, and governance practices.

This framework supports:

- Oracle
- PostgreSQL
- Apache NiFi
- Apache Kafka
- ETL Pipelines
- AI Pipelines
- RAG Applications

---

# Why Data Quality Matters

Every AI pipeline depends on trusted data.

```

Source Systems
│
▼
Data Quality
│
▼
ETL
│
▼
Chunking
│
▼
Embeddings
│
▼
Vector Database
│
▼
Retriever
│
▼
LLM

```

If poor-quality data enters the pipeline:

- Wrong embeddings are generated.
- Incorrect documents are retrieved.
- LLM responses become inaccurate.
- Hallucinations increase.
- Business trust decreases.

---

# Data Quality Dimensions

| Dimension | Description |
|------------|-------------|
| Completeness | Required data exists |
| Accuracy | Data correctly represents reality |
| Consistency | Data is consistent across systems |
| Validity | Data conforms to expected formats |
| Uniqueness | No duplicate records |
| Timeliness | Data is current |
| Integrity | Relationships are preserved |
| Availability | Data is accessible |

---

# Enterprise Data Quality Lifecycle

```

Data Collection
│
▼
Profiling
│
▼
Quality Rules
│
▼
Validation
│
▼
Issue Detection
│
▼
Correction
│
▼
Monitoring
│
▼
Reporting

```

---

# Data Quality Categories

## Schema Validation

Validate

- Table exists
- Columns exist
- Data types
- Constraints
- Nullable columns

---

## Record Validation

Validate

- Missing records
- Duplicate records
- Invalid values
- Mandatory fields

---

## Business Rule Validation

Examples

- Customer Age ≥ 18
- Invoice Amount > 0
- Status in ('ACTIVE','INACTIVE')

---

## Reference Data Validation

Validate

- Country Codes
- Currency Codes
- Product Codes
- Lookup Tables

---

## Relationship Validation

Validate

- Parent-child relationships
- Foreign keys
- Orphan records

---

# Data Profiling

Before creating validation rules, profile the dataset.

Collect:

- Row count
- NULL percentage
- Distinct values
- Min / Max
- Average
- Distribution
- Cardinality

---

# Great Expectations

Recommended for

- Dataset validation
- Data contracts
- Batch validation
- CI/CD integration

Typical Expectations

- expect_table_row_count_to_be_between
- expect_column_values_to_not_be_null
- expect_column_values_to_be_unique
- expect_column_values_to_match_regex

---

# Pandera

Recommended for

- DataFrame validation
- Python ETL
- ML pipelines

Example validations

- Schema
- Data types
- Value ranges
- Nullable columns

---

# AI Data Quality

Before generating embeddings verify:

✓ Text exists

✓ Metadata exists

✓ Language supported

✓ No duplicate documents

✓ Encoding valid

✓ Document size acceptable

---

# Data Quality Metrics

| Metric | Description |
|----------|-------------|
| Completeness Score | % populated fields |
| Accuracy Score | % correct records |
| Duplicate Rate | Duplicate percentage |
| Freshness | Data age |
| Integrity Score | Relationship validity |
| AI Readiness Score | AI-compatible documents |

---

# Automation Strategy

| Layer | Tool |
|--------|------|
| SQL | SQL Scripts |
| Database | pytest |
| DataFrame | Pandera |
| Dataset | Great Expectations |
| CI/CD | GitHub Actions |

---

# Deliverables

- Data Profiling Report
- Data Quality Rules
- Validation Report
- Exception Report
- AI Readiness Report

---

# Best Practices

- Profile before validating.
- Validate before ETL.
- Validate after ETL.
- Monitor continuously.
- Automate quality checks.
- Treat data quality failures as release blockers.

---

# Common Data Quality Issues

| Issue | Impact on AI |
|---------|--------------|
| NULL Text | Missing embeddings |
| Duplicate Documents | Duplicate retrieval |
| Incorrect Metadata | Wrong context |
| Invalid Encoding | Chunk failures |
| Missing IDs | Broken references |
| Stale Data | Outdated responses |

---

# Related Documents

- ETL-Testing-Strategy.md
- Chunking.md
- Embeddings.md
- SQL-Validation-Library.md
