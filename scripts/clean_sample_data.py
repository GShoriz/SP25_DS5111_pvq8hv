import os
import pandas as pd
import re

# Define project directories
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_dir = os.path.join(base_dir, 'sample_data')
seeds_dir = os.path.join(base_dir, 'projects', 'gainers', 'seeds')
os.makedirs(seeds_dir, exist_ok=True)

# File list
file_names = [
    'sanalysisgainers2025-04-04_21-33.csv',
    'wsjgainers2025-04-02_13-33.csv',
    'yahoogainers2025-04-02_19-01.csv',
    'sanalysisgainers2025-04-04_20-34.csv',
    'sanalysisgainers2025-04-04_21-01.csv'
]

# Clean column names
def clean_column_names(columns):
    return [re.sub(r'\W+', '_', col.strip().lower()).strip('_') for col in columns]

# Clean values
def clean_row_values(series):
    return series.apply(lambda x: re.sub(r'\W+', '_', str(x).strip().lower()) if isinstance(x, str) else x)

# Process each file
for file_name in file_names:
    input_path = os.path.join(data_dir, file_name)
    df = pd.read_csv(input_path, encoding='utf-8')

    # Clean headers
    df.columns = clean_column_names(df.columns)

    # Keep only the selected columns for yahoogainers
    if file_name == 'yahoogainers2025-04-02_19-01.csv':
        keep_cols = ['symbol', 'name', 'change', 'volume', 'market_cap']
        df = df[[col for col in keep_cols if col in df.columns]]

    # Clean row values
    df = df.apply(clean_row_values, axis=0)

    # Clean and save filename
    cleaned_name = re.sub(r'\W+', '_', os.path.splitext(file_name)[0].lower()).strip('_') + '.csv'
    output_path = os.path.join(seeds_dir, cleaned_name)
    df.to_csv(output_path, index=False)
    print(f"Saved cleaned file: {output_path}")
