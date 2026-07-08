"""
Reusable RAG Validation Utilities
"""


def validate_similarity(score):

    return score >= 0.80


def validate_groundedness(flag):

    return flag is True


def validate_hallucination(flag):

    return flag is False


def validate_citations(count):

    return count > 0


def validate_answer(answer):

    return answer.strip() != ""