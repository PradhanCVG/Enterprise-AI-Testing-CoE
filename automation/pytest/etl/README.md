# ETL Automation Framework

## Overview

The ETL Automation Framework provides automated validation for Enterprise ETL pipelines using **pytest**.

It validates data movement from source systems (Oracle, APIs, Files, Kafka, etc.) to target systems (PostgreSQL, Data Warehouse, Lakehouse, etc.).

The framework is designed to support:

- Oracle
- PostgreSQL
- Apache NiFi
- Apache Kafka
- Batch ETL
- Incremental ETL
- CDC (Change Data Capture)
- Enterprise AI Data Pipelines

---

# Folder Structure

```
etl/

├── README.md
├── sample_data/
├── expected_results/
├── test_pipeline.py
├── test_reconciliation.py
├── test_incremental_load.py
├── test_duplicate_detection.py
├── test_data_transformation.py
├── test_batch_statistics.py
├── test_file_validation.py
└── etl_validation_queries.sql
```

---

# Test Coverage

## Pipeline Validation

- Source connectivity
- Target connectivity
- Source table validation
- Target table validation
- Pipeline execution

---

## Reconciliation

- Record Count
- Column Count
- Primary Keys
- NULL Values
- Duplicate Records

---

## Incremental Load

- CDC Validation
- Delta Records
- Timestamp Validation
- Latest Load Validation

---

## Data Transformation

- Business Rules
- Lookup Validation
- Derived Columns
- Data Type Conversion

---

## Batch Statistics

- Batch Execution
- Batch Status
- Execution Time
- Success Rate

---

## File Validation

- File Exists
- File Format
- File Size
- Header Validation

---

# Running Tests

Run all ETL tests

```bash
pytest etl/
```

Run a single test

```bash
pytest etl/test_pipeline.py
```

Run with verbose output

```bash
pytest -v etl/
```

Run HTML Report

```bash
pytest --html=reports/etl_report.html
```

---

# Supported Databases

- Oracle
- PostgreSQL

---

# Supported ETL Platforms

- Apache NiFi
- Apache Kafka
- Informatica
- Talend
- SSIS
- Custom ETL Pipelines

---

# Best Practices

- Validate source before ETL execution.
- Perform reconciliation after every load.
- Automate regression testing.
- Monitor batch statistics.
- Validate incremental loads separately.
- Store expected results under version control.
- Integrate ETL tests into CI/CD pipelines.