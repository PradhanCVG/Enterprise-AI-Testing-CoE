"""
Embedding Validation Utilities
"""


def validate_dimension(embedding, expected):

    return len(embedding) == expected


def validate_not_empty(embedding):

    return len(embedding) > 0


def validate_numeric(embedding):

    return all(isinstance(x, float) for x in embedding)


def validate_similarity(score):

    return 0 <= score <= 1


def validate_drift(score, threshold=0.05):

    return score < threshold