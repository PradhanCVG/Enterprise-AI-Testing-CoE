"""
Reusable Vector Validation Utilities
"""


def validate_similarity(score):

    return 0 <= score <= 1


def validate_top_k(results, k):

    return len(results) == k


def validate_metadata(metadata):

    required = [
        "document",
        "page"
    ]

    return all(field in metadata for field in required)


def validate_vector(vector):

    return len(vector) > 0