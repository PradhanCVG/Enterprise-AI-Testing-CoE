# Guardrails Automation Framework

## Overview

This module validates AI safety, security, and compliance for Enterprise AI applications.

## Test Coverage

- Prompt Injection
- Jailbreak Detection
- PII Detection
- Toxicity Detection
- Sensitive Data Protection
- Content Safety
- Policy Compliance
- Input Validation
- Output Validation
- Rate Limiting

## Supported Frameworks

- OpenAI Guardrails
- Azure AI Content Safety
- NVIDIA NeMo Guardrails
- LangChain Guardrails
- Custom Enterprise Policies

## Execute

```bash
pytest guardrails/
```

Generate HTML Report

```bash
pytest guardrails/ --html=reports/guardrails_report.html
```