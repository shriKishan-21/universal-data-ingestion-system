import pandas as pd

def clean_data(df):
    df = df.drop_duplicates()
    df.columns = df.columns.str.lower().str.replace(" ","_")
    df = df.fillna("NA")
    return df