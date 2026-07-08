"""
Database Utilities

Supports

- Oracle
- PostgreSQL
"""

import oracledb
import psycopg


class OracleDB:

    def __init__(
        self,
        host,
        port,
        service,
        username,
        password,
    ):

        self.connection = None

        self.host = host
        self.port = port
        self.service = service
        self.username = username
        self.password = password

    def connect(self):

        dsn = f"{self.host}:{self.port}/{self.service}"

        self.connection = oracledb.connect(
            user=self.username,
            password=self.password,
            dsn=dsn,
        )

    def execute(self, sql):

        cursor = self.connection.cursor()

        cursor.execute(sql)

        return cursor.fetchall()

    def close(self):

        if self.connection:
            self.connection.close()


class PostgreSQLDB:

    def __init__(
        self,
        host,
        port,
        database,
        username,
        password,
    ):

        self.connection = None

        self.host = host
        self.port = port
        self.database = database
        self.username = username
        self.password = password

    def connect(self):

        self.connection = psycopg.connect(
            host=self.host,
            port=self.port,
            dbname=self.database,
            user=self.username,
            password=self.password,
        )

    def execute(self, sql):

        cursor = self.connection.cursor()

        cursor.execute(sql)

        return cursor.fetchall()

    def close(self):

        if self.connection:
            self.connection.close()