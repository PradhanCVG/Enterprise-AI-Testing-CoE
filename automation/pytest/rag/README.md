# RAG Automation Framework

## Overview

This module validates Retrieval-Augmented Generation (RAG) pipelines by testing retrieval quality, context construction, grounding, relevance, faithfulness, hallucination detection, citations, prompt construction, and end-to-end response generation.

## Test Coverage

- Retrieval Validation
- Context Validation
- Groundedness
- Relevance
- Hallucination Detection
- Faithfulness
- Answer Quality
- Citation Validation
- Prompt Construction
- End-to-End Pipeline Testing

## Supported Frameworks

- LangChain
- LlamaIndex
- Haystack
- Azure AI Search
- OpenAI
- PGVector
- Pinecone
- Milvus

## Execute

```bash
pytest rag/
```

Generate HTML Report

```bash
pytest rag/ --html=reports/rag_report.html
```