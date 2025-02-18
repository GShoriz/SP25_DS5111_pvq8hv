import sys
sys.path.append('..')
import bin.normalize_csv as normalize_csv
import pandas as pd

def test_load_and_process_csv():
    # Create a sample DataFrame similar to normalize_csv.py
    sample_data = {
        'Symbol': ['AAPL', 'MSFT'],
        'Price': [150.50, 250.75],
        'Change': [1.50, 2.50],
        'Change %': [1.00, 2.00]
    }
    df = pd.DataFrame(sample_data)

    # Mimic the processing steps 
    processed_df = normalize_csv.extract_required_columns(df)

    # Check that the DataFrame contains the right columns after processing
    expected_columns = ['symbol', 'price', 'price_change', 'price_percent_change']
    assert list(processed_df.columns) == expected_columns, "Processed DataFrame does not contain the expected columns"
