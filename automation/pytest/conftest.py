"""
Enterprise AI Testing CoE

Global pytest fixtures

Author : Enterprise AI Testing CoE
"""

import os
import pytest

from utils.config import Config
from utils.logger import get_logger
from utils.db import OracleDB
from utils.db import PostgreSQLDB

logger = get_logger(__name__)


@pytest.fixture(scope="session")
def config():
    """
    Load framework configuration.
    """
    return Config()


@pytest.fixture(scope="session")
def oracle_db(config):
    """
    Create Oracle connection.
    """

    db = OracleDB(
        host=config.ORACLE_HOST,
        port=config.ORACLE_PORT,
        service=config.ORACLE_SERVICE,
        username=config.ORACLE_USER,
        password=config.ORACLE_PASSWORD,
    )

    logger.info("Connecting to Oracle...")

    db.connect()

    yield db

    logger.info("Closing Oracle connection...")

    db.close()


@pytest.fixture(scope="session")
def postgres_db(config):
    """
    Create PostgreSQL connection.
    """

    db = PostgreSQLDB(
        host=config.POSTGRES_HOST,
        port=config.POSTGRES_PORT,
        database=config.POSTGRES_DATABASE,
        username=config.POSTGRES_USER,
        password=config.POSTGRES_PASSWORD,
    )

    logger.info("Connecting to PostgreSQL...")

    db.connect()

    yield db

    logger.info("Closing PostgreSQL connection...")

    db.close()