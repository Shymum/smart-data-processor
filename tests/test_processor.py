from io import BytesIO
import pandas as pd
import pytest
from processor import read_table, clean_table, combine_tables, to_xlsx


def test_clean_and_combine():
    a = pd.DataFrame({'name': [' Alice ', 'Alice', '  '], 'n': [1, 1, None]})
    b = pd.DataFrame({'name': ['Bob'], 'extra': [2]})
    result = clean_table(combine_tables([a, b]))
    assert result['name'].tolist() == ['Alice', 'Bob']
    assert 'extra' in result.columns


def test_csv_and_excel_roundtrip():
    frame = read_table(BytesIO(b'name,n\nAlice,1\n'), 'sample.csv')
    restored = read_table(BytesIO(to_xlsx(frame)), 'sample.xlsx')
    pd.testing.assert_frame_equal(frame, restored)


def test_invalid_input():
    with pytest.raises(ValueError):
        read_table(BytesIO(b''), 'file.txt')
    with pytest.raises(ValueError):
        combine_tables([])
