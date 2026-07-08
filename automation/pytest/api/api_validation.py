"""
API Validation Utilities
"""


def validate_status(code):

    return code == 200


def validate_latency(latency):

    return latency < 2


def validate_authentication(flag):

    return flag


def validate_schema(response):

    return "status" in response


def validate_availability(value):

    return value >= 99.9