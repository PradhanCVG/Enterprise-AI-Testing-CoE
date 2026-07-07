# SQL Validation Library

> *A reusable collection of SQL validation techniques for Oracle and PostgreSQL databases supporting Enterprise AI, ETL, and Data Engineering platforms.*

---

# Purpose

The SQL Validation Library provides standardized SQL validation techniques that help verify the integrity, quality, consistency, and readiness of enterprise databases before they are consumed by ETL pipelines, AI models, Vector Databases, and Retrieval-Augmented Generation (RAG) systems.

Rather than embedding SQL inside documentation, this guide references reusable SQL scripts maintained under the `sql/` directory.

These scripts can be executed manually, scheduled through automation, or integrated into CI/CD pipelines.

---

# Objectives

The SQL Validation Library aims to:

- Standardize database validation across Oracle and PostgreSQL
- Detect data quality issues before ETL execution
- Ensure AI-ready datasets
- Support reusable automation
- Reduce production defects
- Enable continuous database health validation

---

# Validation Categories

| Category | Oracle | PostgreSQL | Automation |
|-----------|:------:|:----------:|:----------:|
| Connectivity | ✅ | ✅ | pytest |
| Schema Validation | ✅ | ✅ | pytest |
| Tables & Views | ✅ | ✅ | pytest |
| Constraints | ✅ | ✅ | pytest |
| Index Validation | ✅ | ✅ | pytest |
| Partition Validation | ✅ | ✅ | pytest |
| Data Quality | ✅ | ✅ | Great Expectations |
| Duplicate Detection | ✅ | ✅ | SQL |
| Referential Integrity | ✅ | ✅ | SQL |
| ETL Validation | ✅ | ✅ | pytest |
| Incremental Load | ✅ | ✅ | SQL |
| Data Freshness | ✅ | ✅ | SQL |
| Performance | ✅ | ✅ | pytest |
| Security | ✅ | ✅ | SQL |
| JSON Validation | — | ✅ | pytest |
| PGVector Validation | — | ✅ | pytest |

---

# Validation Workflow

```text
Database Connection
        │
        ▼
Schema Validation
        │
        ▼
Table Validation
        │
        ▼
Constraint Validation
        │
        ▼
Partition Validation
        │
        ▼
Performance Validation
        │
        ▼
Security Validation
        │
        ▼
AI Readiness Validation
        │
        ▼
ETL / AI Pipeline
```

---

# SQL Validation Script Order

Use the following ordered script sequence for each database platform. This is the recommended execution order for validation.

## Oracle

- `sql/oracle/connectivity.sql`
- `sql/oracle/schema_validation.sql`
- `sql/oracle/table_validation.sql`
- `sql/oracle/constraint_validation.sql`
- `sql/oracle/partition_validation.sql`
- `sql/oracle/performance_validation.sql`
- `sql/oracle/security_validation.sql`
- `sql/oracle/ai_readiness.sql`

## PostgreSQL

- `sql/postgresql/connectivity.sql`
- `sql/postgresql/schema_validation.sql`
- `sql/postgresql/table_validation.sql`
- `sql/postgresql/constraint_validation.sql`
- `sql/postgresql/jsonb_validation.sql`
- `sql/postgresql/pgvector_validation.sql`
- `sql/postgresql/performance_validation.sql`
- `sql/postgresql/security_validation.sql`
- `sql/postgresql/ai_readiness.sql`

---

# 1. Connectivity Validation

## Purpose

Verify that the target database is accessible before executing validation or ETL jobs.

### Validate

- Database availability
- User authentication
- Network connectivity
- Database version
- Current database time
- Session information

### SQL Scripts

```text
sql/oracle/connectivity.sql
sql/postgresql/connectivity.sql
```

---

# 2. Schema Validation

## Purpose

Ensure all required database objects exist.

### Validate

- Schemas
- Tables
- Views
- Materialized Views
- Packages (Oracle)
- Functions
- Procedures
- Triggers
- Sequences

### SQL Scripts

```text
sql/oracle/schema_validation.sql
sql/postgresql/schema_validation.sql
```

---

# 3. Table Validation

## Validate

- Missing tables
- Empty tables
- Unexpected tables
- Record counts
- Growth trends

### SQL Scripts

```text
sql/oracle/table_validation.sql
sql/postgresql/table_validation.sql
```

# 📄 `sql/postgresql/table_validation.sql`

```

```

---

# 4. Column Validation

Validate

- Missing columns
- Incorrect datatype
- Nullable columns
- Default values
- Column length

---

# 5. Constraint Validation

Validate

- Primary Keys
- Foreign Keys
- Unique Constraints
- Check Constraints
- NOT NULL Constraints

### SQL Scripts

```text
sql/oracle/constraint_validation.sql
sql/postgresql/constraint_validation.sql
```

---

# 6. Index Validation

Validate

- Missing indexes
- Invalid indexes
- Fragmented indexes
- Index usage
- Duplicate indexes

---

# 7. Partition Validation

## Oracle

- Range Partitions
- Interval Partitions
- Hash Partitions
- Composite Partitions

## PostgreSQL

- Range
- Hash
- List

Validate

- Missing partitions
- Future partitions
- Partition pruning
- Default partitions

---

# 8. Data Quality Validation

Validate

- NULL values
- Duplicate records
- Invalid values
- Mandatory fields
- Domain validation
- Reference data

Recommended Tools

- Great Expectations
- Pandera

---

# 9. Referential Integrity Validation

Validate

- Orphan records
- Invalid foreign keys
- Missing parent rows
- Circular references

---

# 10. ETL Validation

Validate

- Source-to-target reconciliation
- Record counts
- Checksums
- Transformation accuracy
- Duplicate detection

---

# 11. Incremental Load Validation

Validate

- Delta records
- Last update timestamps
- Missing transactions
- Duplicate processing

---

# 12. Data Freshness Validation

Validate

- Latest business date
- Latest load timestamp
- Data lag
- SLA compliance

---

# 13. AI Readiness Validation

Before data is converted into embeddings, verify:

- No NULL text
- Required metadata exists
- Unique document IDs
- Valid encoding
- Supported language
- No duplicate documents

---

# 14. PGVector Validation

Applicable to PostgreSQL.

Validate

- Vector dimensions
- NULL embeddings
- Embedding count
- Index health
- Similarity search
- Query latency

---

# 15. Performance Validation

Validate

- Execution plans
- Index usage
- Slow queries
- Full table scans
- Lock contention
- Statistics freshness

---

# 16. Security Validation

Validate

- Database users
- Roles
- Privileges
- Password policies
- Encryption
- Audit settings

---

# Automation Strategy

| Layer | Tool |
|--------|------|
| SQL Execution | pytest |
| Oracle | python-oracledb |
| PostgreSQL | psycopg |
| ORM | SQLAlchemy |
| Data Quality | Great Expectations |
| DataFrames | Pandera |
| CI/CD | GitHub Actions |

---

# Deliverables

Each validation cycle should generate:

- Connectivity Report
- Schema Validation Report
- Data Quality Report
- Constraint Validation Report
- Performance Report
- Security Report
- AI Readiness Report
- Validation Summary

---

# Best Practices

- Keep SQL scripts independent of documentation.
- Store reusable SQL under the `sql/` directory.
- Automate SQL execution using pytest.
- Run database validation before ETL execution.
- Validate AI readiness before embedding generation.
- Version control every SQL script.
- Include SQL validation in CI/CD pipelines.

---

# Repository Mapping

```text
docs/
└── 04-Database-Testing/
    ├── SQL-Validation-Library.md

sql/
├── oracle/
│   ├── connectivity.sql
│   ├── schema_validation.sql
│   ├── table_validation.sql
│   ├── constraint_validation.sql
│   ├── partition_validation.sql
│   ├── performance_validation.sql
│   ├── security_validation.sql
│   └── ai_readiness.sql
│
└── postgresql/
    ├── connectivity.sql
    ├── schema_validation.sql
    ├── table_validation.sql
    ├── constraint_validation.sql
    ├── jsonb_validation.sql
    ├── pgvector_validation.sql
    ├── performance_validation.sql
    ├── security_validation.sql
    └── ai_readiness.sql
```

---

# Related Documents

- Database-Testing-Overview.md
- Oracle-Database-Testing.md
- PostgreSQL-Database-Testing.md
- Database-Test-Cases.md
- ETL-Testing-Strategy.md