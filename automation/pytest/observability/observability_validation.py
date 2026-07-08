"""
Observability Validation Utilities
"""


def validate_latency(value):
    return value < 5


def validate_cost(cost):
    return cost >= 0


def validate_drift(score):
    return score < 0.05


def validate_health(cpu, memory):
    return cpu < 80 and memory < 85


def validate_logging(flag):
    return flag is True