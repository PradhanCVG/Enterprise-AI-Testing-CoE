"""
Evaluation Validation Utilities
"""


def validate_score(score, minimum=0.85):
    return score >= minimum


def validate_boolean(flag):
    return flag is True


def validate_bias(score):
    return score < 0.05


def validate_hallucination(flag):
    return flag is False


def validate_sql(sql):
    return sql.upper().startswith("SELECT")