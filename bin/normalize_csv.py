"""
This py file provides functionalities to normalize CSV files that contain stock data.
It ensures that only required columns are extracted and normalized into a consistent format.
"""

import sys
import pandas as pd

def load_csv(file_path):
    """Load a CSV file and return a pandas DataFrame."""
    assert isinstance(file_path, str), f"Expected string for file_path, got {type(file_path)}"
    try:
        data_frame = pd.read_csv(file_path)
        assert not data_frame.empty, "Loaded CSV file is empty"
        return data_frame
    except FileNotFoundError as exc:
        raise FileNotFoundError(f"The file {file_path} could not be found.") from exc

def extract_required_columns(data_frame):
    """Extract and rename the required columns from the DataFrame."""
    required_columns = ['Symbol', 'Price', 'Change', 'Change %']
    assert all(column in data_frame.columns for column in required_columns), \
           "Data frame does not contain all the required columns."
    data_frame = data_frame[required_columns]
    data_frame.columns = ['symbol', 'price', 'price_change', 'price_percent_change']
    return data_frame

def save_normalized_csv(data_frame, original_path):
    """Save the DataFrame to a new CSV file with '_norm' appended to the filename."""
    assert isinstance(data_frame, pd.DataFrame), "Input must be a pandas DataFrame"
    new_file_path = original_path.replace('.csv', '_norm.csv')
    data_frame.to_csv(new_file_path, index=False)
    return new_file_path

def normalize_csv(file_path):
    """Process the CSV file to normalize it."""
    data_frame = load_csv(file_path)
    data_frame = extract_required_columns(data_frame)
    new_file_path = save_normalized_csv(data_frame, file_path)
    assert pd.read_csv(new_file_path).equals(data_frame), \
	 "The saved file does not match the expected data"
    print(f"Normalized CSV saved as {new_file_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python normalize_csv.py <path to raw gainers csv>", file=sys.stderr)
        sys.exit(1)
    normalize_csv(sys.argv[1])
