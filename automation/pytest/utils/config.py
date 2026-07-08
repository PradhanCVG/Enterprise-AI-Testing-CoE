"""
Configuration Loader
"""

import os
from dotenv import load_dotenv

load_dotenv()


class Config:

    ORACLE_HOST = os.getenv("ORACLE_HOST")
    ORACLE_PORT = int(os.getenv("ORACLE_PORT", 1521))
    ORACLE_SERVICE = os.getenv("ORACLE_SERVICE")
    ORACLE_USER = os.getenv("ORACLE_USER")
    ORACLE_PASSWORD = os.getenv("ORACLE_PASSWORD")

    POSTGRES_HOST = os.getenv("POSTGRES_HOST")
    POSTGRES_PORT = int(os.getenv("POSTGRES_PORT", 5432))
    POSTGRES_DATABASE = os.getenv("POSTGRES_DATABASE")
    POSTGRES_USER = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")