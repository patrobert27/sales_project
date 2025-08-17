import pandas as pd

def load_data(path):
    try:
        return pd.read_csv(path)
    except FileNotFoundError:
        print(f"Archivo {path} no encontrado.")
        return pd.DataFrame()
    except Exception:
        print(f"Error inesperado.")
        return pd.DataFrame()

def clean_sales(df):
    # df porque DataFrame es el tipo de objeto principal de pandas
    df = df.dropna()
    df = df.drop_duplicates()
    return df
