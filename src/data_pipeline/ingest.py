import pandas as pd
from pathlib import Path

def load_csv(filepath: str):
    df = pd.read_csv(filepath, parse_dates=['timestamp'])
    return df

if __name__ == '__main__':
    df = load_csv('data/raw/aq_sample.csv')
    print(df.head())
