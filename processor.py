"""Small, independently testable table processing functions."""
from io import BytesIO
import pandas as pd


def read_table(source, name):
    if name.lower().endswith('.csv'):
        return pd.read_csv(source)
    if name.lower().endswith('.xlsx'):
        return pd.read_excel(source)
    raise ValueError('Only CSV and XLSX files are supported')


def clean_table(frame, trim=True, drop_empty=True, deduplicate=True):
    result = frame.copy()
    if trim:
        for col in result.select_dtypes(include=['object', 'string']).columns:
            result[col] = result[col].map(lambda x: x.strip() if isinstance(x, str) else x)
        result = result.replace(r'^\s*$', float('nan'), regex=True)
    if drop_empty:
        result = result.dropna(how='all')
    if deduplicate:
        result = result.drop_duplicates()
    return result.reset_index(drop=True)


def combine_tables(frames):
    if not frames:
        raise ValueError('Upload at least one table')
    return pd.concat(frames, ignore_index=True, sort=False)


def to_xlsx(frame):
    output = BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        frame.to_excel(writer, index=False, sheet_name='Data')
    return output.getvalue()
