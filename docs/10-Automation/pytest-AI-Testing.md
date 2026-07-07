# AI Testing Automation with pytest

> *A practical guide to building automated test suites for Enterprise AI applications using pytest.*

---

# Purpose

This document explains how to use **pytest** as the primary automation framework for Enterprise AI Testing.

The framework provides a standardized approach for automating:

- Database Testing
- ETL Testing
- Data Quality
- Chunking
- Embedding Validation
- Vector Database Testing
- RAG Evaluation
- Guardrail Testing
- API Testing

The goal is to build reusable, maintainable, and scalable automated test suites that integrate seamlessly into CI/CD pipelines.

---

# Why pytest?

pytest is lightweight, extensible, and widely adopted for Python-based testing.

Benefits include:

- Simple syntax
- Parameterized testing
- Rich assertion support
- Plugin ecosystem
- HTML reporting
- CI/CD integration
- Easy integration with AI evaluation frameworks

---

# Enterprise AI Automation Architecture

```text
pytest
    │
    ├── Database Tests
    │
    ├── ETL Tests
    │
    ├── Data Quality Tests
    │
    ├── Chunking Tests
    │
    ├── Embedding Tests
    │
    ├── Vector DB Tests
    │
    ├── RAG Tests
    │
    ├── Guardrail Tests
    │
    └── API Tests
```

---

# Recommended Project Structure

```
automation/

pytest/

├── conftest.py

├── database/

│     test_connectivity.py

│     test_schema.py

│     test_constraints.py

│     test_data_quality.py

├── etl/

│     test_etl_pipeline.py

│     test_reconciliation.py

├── chunking/

│     test_chunk_size.py

│     test_chunk_overlap.py

│     test_metadata.py

├── embeddings/

│     test_embedding_generation.py

│     test_embedding_dimensions.py

│     test_similarity.py

├── vector_db/

│     test_vector_insert.py

│     test_similarity_search.py

│     test_top_k.py

├── rag/

│     test_retrieval.py

│     test_groundedness.py

│     test_hallucination.py

├── guardrails/

│     test_prompt_injection.py

│     test_pii.py

│     test_policy.py

└── reports/
```

---

# pytest Installation

```bash
pip install pytest
pip install pytest-html
pip install pytest-xdist
pip install pytest-cov
```

Recommended plugins

- pytest-html
- pytest-cov
- pytest-xdist
- pytest-rerunfailures
- pytest-mock

---

# Database Testing Example

Example

```python
def test_database_connection(db_connection):
    assert db_connection.is_connected()
```

Expected

Database connection established successfully.

---

# ETL Testing Example

Validate record counts after ETL execution.

```python
def test_record_count():

    assert source_count == target_count
```

---

# Data Quality Example

```python
def test_no_null_customer_id():

    assert null_count == 0
```

---

# Chunking Example

```python
def test_chunk_size():

    assert chunk_size <= 500
```

---

# Embedding Validation Example

```python
def test_embedding_dimension():

    assert len(vector) == 1536
```

---

# Similarity Validation Example

```python
def test_similarity():

    assert similarity > 0.90
```

---

# Vector Database Example

```python
def test_vector_search():

    assert retrieved_documents > 0
```

---

# RAG Evaluation Example

```python
def test_groundedness():

    assert groundedness_score > 0.95
```

---

# Guardrail Example

```python
def test_prompt_injection():

    assert blocked is True
```

---

# API Testing Example

```python
def test_chat_endpoint():

    response = client.post("/chat")

    assert response.status_code == 200
```

---

# Fixtures

Common fixtures

- Database Connection
- API Client
- Test Dataset
- Gold Dataset
- Embedding Model
- Vector Database Client

Store fixtures inside

```
conftest.py
```

---

# Parameterized Testing

Example

```python
@pytest.mark.parametrize(
    "question",
    [
        "Refund Policy",
        "Leave Policy",
        "Travel Policy"
    ]
)
```

Useful for evaluating many prompts using the same test logic.

---

# Test Markers

Recommended markers

```python
@pytest.mark.database

@pytest.mark.etl

@pytest.mark.chunking

@pytest.mark.embedding

@pytest.mark.vector

@pytest.mark.rag

@pytest.mark.guardrail

@pytest.mark.performance
```

Execute specific suites

```bash
pytest -m database

pytest -m rag
```

---

# Reporting

Generate HTML reports

```bash
pytest --html=report.html
```

Coverage

```bash
pytest --cov
```

JUnit

```bash
pytest --junitxml=results.xml
```

---

# CI/CD Integration

Typical workflow

```
Git Commit

↓

GitHub Actions

↓

pytest

↓

HTML Report

↓

Quality Gates

↓

Deployment
```

---

# Best Practices

- Use fixtures for reusable setup.
- Keep tests independent.
- Separate unit, integration, and AI evaluation tests.
- Parameterize repetitive test cases.
- Run tests in parallel when possible.
- Publish reports after every execution.

---

# Common Anti-Patterns

- Hard-coded test data.
- Shared mutable state.
- Mixing functional and performance tests.
- Ignoring flaky AI tests.
- No regression datasets.
- No automated reporting.

---

# Deliverables

- Automated pytest Framework
- HTML Test Report
- Coverage Report
- AI Evaluation Report
- Release Validation Report

---

# Related Documents

- Automation-Framework.md
- GitHub-Actions.md
- DeepEval.md
- Ragas.md