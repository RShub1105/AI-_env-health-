import pandas as pd

def basic_clean(df: pd.DataFrame):
    df = df.sort_values('timestamp').reset_index(drop=True)
    df = df.fillna(method='ffill').fillna(method='bfill')
    return df

if __name__ == '__main__':
    df = pd.read_csv('data/raw/aq_sample.csv', parse_dates=['timestamp'])
    from pathlib import Path
    Path('data/processed').mkdir(parents=True, exist_ok=True)
    df = basic_clean(df)
    df.to_csv('data/processed/aq_processed.csv', index=False)
    print("✅ Cleaned data saved to data/processed/aq_processed.csv")

