# Ragas for Enterprise RAG Evaluation

> *Ragas is an evaluation framework specifically designed for Retrieval-Augmented Generation (RAG) systems. It measures the quality of retrieval, context, and AI-generated responses using automated metrics.*

---

# Purpose

This document explains how Ragas can be integrated into the Enterprise AI Testing Framework to evaluate Retrieval-Augmented Generation (RAG) systems.

Unlike traditional testing frameworks, Ragas focuses on the relationship between:

- User Question
- Retrieved Context
- AI Response
- Ground Truth

This enables objective measurement of RAG quality.

---

# Why Ragas?

Large Language Models can generate convincing answers even when retrieval is poor.

Ragas helps answer questions such as:

- Did the retriever find the correct documents?
- Was enough context retrieved?
- Was the answer supported by the retrieved context?
- Is the answer relevant to the user's question?
- Has retrieval quality degraded after changes?

---

# Where Ragas Fits

```
Enterprise Documents
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
Retrieved Context
        │
        ▼
LLM
        │
        ▼
Generated Answer
        │
        ▼
Ragas Evaluation
```

---

# Enterprise RAG Evaluation Flow

```
Question

↓

Retriever

↓

Retrieved Chunks

↓

Prompt

↓

LLM

↓

Answer

↓

Ragas Metrics

↓

Evaluation Report
```

---

# Ragas Evaluation Metrics

| Metric | Purpose |
|----------|----------|
| Context Precision | Measures relevance of retrieved chunks |
| Context Recall | Measures completeness of retrieved information |
| Faithfulness | Checks whether the response is supported by the retrieved context |
| Answer Relevancy | Measures how well the response answers the user's question |
| Answer Correctness | Compares the response against the expected answer |
| Context Utilization | Measures whether the retrieved context was actually used |

---

# Metric Details

## Context Precision

Question

```
What is the employee leave policy?
```

Retrieved Documents

- Employee Leave Policy ✅
- Travel Policy ❌
- Payroll Guide ❌

Precision

```
Relevant Documents

÷

Retrieved Documents
```

Higher precision means less irrelevant context.

---

## Context Recall

Expected Documents

- Employee Leave Policy
- HR Handbook

Retrieved

- Employee Leave Policy

Recall

```
Retrieved Relevant Documents

÷

Expected Relevant Documents
```

Higher recall means more complete retrieval.

---

## Faithfulness

Checks whether every statement in the answer can be traced back to the retrieved context.

Example

Context

```
Employees receive 20 days annual leave.
```

Response

```
Employees receive 20 days annual leave.
```

Expected

High Faithfulness

---

## Answer Relevancy

Measures whether the generated answer actually addresses the user's question.

Poor Example

Question

```
How do I reset my password?
```

Answer

```
The employee leave policy allows...
```

Expected

Low Relevancy Score

---

## Answer Correctness

Compare the generated answer with a verified expected answer (Ground Truth).

This metric is especially useful for regression testing.

---

## Context Utilization

Checks whether the LLM actually used the retrieved documents.

Good retrieval is wasted if the response ignores the context.

---

# Gold Dataset

Ragas works best with a curated Gold Dataset.

Example

| Question | Expected Answer | Expected Documents |
|-----------|-----------------|--------------------|
| Refund policy | Refunds allowed within 30 days | Refund Policy v3 |
| Password reset | Follow IAM procedure | IAM User Guide |
| Leave policy | 20 annual leave days | HR Policy |

---

# Regression Testing

Run Ragas after every:

- Model upgrade
- Embedding model change
- Chunking strategy update
- Prompt update
- Vector database migration

Compare evaluation scores against previous releases.

---

# Quality Gates

| Metric | Recommended Target |
|----------|-------------------:|
| Context Precision | ≥ 0.90 |
| Context Recall | ≥ 0.90 |
| Faithfulness | ≥ 0.95 |
| Answer Relevancy | ≥ 0.90 |
| Answer Correctness | ≥ 0.90 |
| Context Utilization | ≥ 0.85 |

---

# Integration with Enterprise AI Testing

```
pytest

↓

DeepEval

↓

Ragas

↓

Generate Reports

↓

Quality Gates

↓

GitHub Actions

↓

Deployment
```

---

# Automation Strategy

Recommended Tools

| Tool | Purpose |
|------|---------|
| pytest | Test orchestration |
| Ragas | RAG evaluation |
| LangChain | Retrieval pipeline |
| LlamaIndex | Knowledge indexing |
| Pandas | Dataset processing |
| GitHub Actions | CI/CD automation |

---

# Test Cases

### TC-RAGAS-001

Validate Context Precision.

Expected

Only relevant documents retrieved.

---

### TC-RAGAS-002

Validate Context Recall.

Expected

All required documents retrieved.

---

### TC-RAGAS-003

Validate Faithfulness.

Expected

Response fully supported by retrieved context.

---

### TC-RAGAS-004

Validate Answer Relevancy.

Expected

Response directly answers the user's question.

---

### TC-RAGAS-005

Validate Answer Correctness.

Expected

Response matches the verified expected answer.

---

### TC-RAGAS-006

Validate Context Utilization.

Expected

Retrieved context contributes to the generated response.

---

# Reporting

Each Ragas execution should generate:

- Evaluation Summary
- Context Precision Report
- Context Recall Report
- Faithfulness Report
- Answer Relevancy Report
- Regression Report

---

# Best Practices

- Maintain version-controlled Gold Datasets.
- Run Ragas after every retrieval or embedding change.
- Combine Ragas with DeepEval for comprehensive evaluation.
- Review failed evaluations manually before deployment.
- Include Ragas in CI/CD quality gates.

---

# Common Anti-Patterns

- Evaluating only the final response.
- Ignoring retrieval quality.
- Using small or biased evaluation datasets.
- Skipping regression testing after model updates.
- Not versioning Gold Datasets.

---

# Deliverables

- Ragas Evaluation Suite
- Gold Dataset
- Evaluation Dashboard
- Regression Report
- Release Readiness Report

---

# Related Documents

- RAG-Testing.md
- DeepEval.md
- AI-Observability.md
- pytest-AI-Testing.md