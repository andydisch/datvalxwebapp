# -*- coding: utf-8 -*-


import pendulum
import dotenv
import psycopg2
import os
import pandas as pd


dotenv.load_dotenv()

DATAPOOL_HOST = os.getenv("datapool_host")
DATAPOOL_USER = os.getenv("datapool_user")
DATAPOOL_PORT = os.getenv("datapool_port")
DATAPOOL_DATABASE = os.getenv("datapool_database")
DATAPOOL_PASSWORD = os.getenv("datapool_password")


def _connect_to_datapool():

    conn = psycopg2.connect(
        host=DATAPOOL_HOST,
        database=DATAPOOL_DATABASE,
        user=DATAPOOL_USER,
        password=DATAPOOL_PASSWORD,
        port=DATAPOOL_PORT,
    )
    cur = conn.cursor()
    yield cur
    cur.close()
    conn.close()


def query_datapool(
    signal: str, variable: str, start: pendulum.datetime, end: pendulum.datetime
) -> pd.DataFrame:

    cur = next(_connect_to_datapool())
    cur.execute(
        f"""
    SELECT signal.timestamp, signal.value
    FROM signal 
    INNER JOIN variable ON signal.variable_id = variable.variable_id
    INNER JOIN source ON signal.source_id = source.source_id
    WHERE variable.name = '{variable}' AND
    source.name = '{signal}' AND
    '{start}'::timestamp <= signal.timestamp AND
    signal.timestamp <= '{end}'::timestamp
    ORDER BY signal.timestamp ASC
    """
    )
    df = pd.DataFrame(cur.fetchall(), columns=["time", "value"])
    df = df.set_index("time")

    return df


def get_last_datapoint(signal: str, variable: str, latest=None) -> pd.DataFrame:

    if not latest:
        latest = pendulum.today("Europe/Zurich").subtract(days=100)

    cur = next(_connect_to_datapool())
    cur.execute(f"""
    SELECT signal.timestamp, signal.value
    FROM signal 
    INNER JOIN variable ON signal.variable_id = variable.variable_id
    INNER JOIN source ON signal.source_id = source.source_id
    WHERE variable.name = '{variable}' AND
    source.name = '{signal}' AND
    '{latest}'::timestamp <= signal.timestamp
    ORDER BY signal.timestamp DESC
    LIMIT 1""")

    df = pd.DataFrame(cur.fetchall(), columns=["time", "value"])
    df = df.set_index("time")

    return df
