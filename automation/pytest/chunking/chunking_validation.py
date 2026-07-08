"""
Enterprise AI Testing CoE

Reusable Chunk Validation Utilities
"""


def validate_chunk_size(chunk,
                        minimum=100,
                        maximum=1000):

    return minimum <= len(chunk) <= maximum


def validate_overlap(overlap,
                     maximum=200):

    return len(overlap) <= maximum


def validate_metadata(metadata):

    required = [
        "source",
        "page",
        "chunk",
        "document_id"
    ]

    return all(key in metadata for key in required)


def validate_not_empty(chunk):

    return chunk.strip() != ""


def validate_semantic_boundary(chunk):

    return chunk.endswith(".") \
        or chunk.endswith(":") \
        or chunk.endswith("!")