# AI Evaluation Framework

## Overview

This module evaluates the quality of AI-generated responses using standard evaluation metrics.

## Test Coverage

- Answer Relevancy
- Faithfulness
- Context Precision
- Context Recall
- Hallucination Detection
- Toxicity Detection
- Bias Evaluation
- Summarization Quality
- SQL Generation
- Code Generation

## Supported Evaluation Frameworks

- DeepEval
- Ragas
- Promptfoo
- LangSmith
- OpenAI Evals

## Execute

```bash
pytest evals/
```

Generate HTML Report

```bash
pytest evals/ --html=reports/evals_report.html
```