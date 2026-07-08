"""
Guardrail Validation Utilities
"""


def validate_pii(flag):
    return flag is True


def validate_toxicity(flag):
    return flag is False


def validate_prompt_injection(flag):
    return flag is True


def validate_policy(flag):
    return flag is True


def validate_output(text):
    return text.strip() != ""