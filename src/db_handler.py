import pandas as pd
from sqlalchemy import create_engine


DB_PATH = "sqlite:///Database/data_store.db"


def store_to_database(df, table_name):
    engine = create_engine(DB_PATH)
    df.to_sql(table_name, engine, if_exists="replace", index=False)


def read_from_database(table_name):
    engine = create_engine(DB_PATH)
    query = f"SELECT * FROM {table_name}"
    return pd.read_sql(query, engine)
