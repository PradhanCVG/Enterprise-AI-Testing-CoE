# Chunking Automation Framework

## Purpose

This module validates document chunking before embedding generation in a Retrieval-Augmented Generation (RAG) pipeline.

## Test Coverage

- Chunk Size Validation
- Chunk Overlap Validation
- Metadata Validation
- Semantic Boundary Validation
- Chunk Quality Validation

## Supported Frameworks

- LangChain
- LlamaIndex
- Haystack
- Custom Chunkers

## Run Tests

```bash
pytest chunking/
```

Run with HTML report

```bash
pytest chunking/ --html=reports/chunking_report.html
```