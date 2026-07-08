# Embedding Automation Framework

## Overview

This module validates embedding generation and quality in Retrieval-Augmented Generation (RAG) pipelines.

## Test Coverage

- Embedding Generation
- Dimension Validation
- Similarity Validation
- Vector Normalization
- Stability Testing
- Drift Detection

## Supported Models

- OpenAI
- Azure OpenAI
- Hugging Face
- Sentence Transformers
- Cohere
- Vertex AI

## Execute

```bash
pytest embeddings/
```

Generate HTML Report

```bash
pytest embeddings/ --html=reports/embedding_report.html
```