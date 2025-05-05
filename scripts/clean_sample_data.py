import os
import pandas as pd

# Define the base directory of your project
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Define the paths
data_dir = os.path.join(base_dir, 'sample_data')
seeds_dir = os.path.join(base_dir, 'projects', 'gainers', 'seeds')

# Ensure the seeds directory exists
os.makedirs(seeds_dir, exist_ok=True)

# List of CSV filenames to process
file_names = [
    'sanalysisgainers2025-04-04_21-33.csv',
    'wsjgainers2025-04-02_13-33.csv',
    'yahoogainers2025-04-02_19-01.csv',
    'sanalysisgainers2025-04-04_20-34.csv',
    'sanalysisgainers2025-04-04_21-01.csv'
]

# Function to clean column names
def clean_column_names(columns):
    return [
        col.strip()
        .lower()
        .replace('%', 'percent')
        .replace(' ', '_')
        .replace('/', '_')
        .replace('-', '_')
        .replace('.', '')
        for col in columns
    ]

# Process each file
for file_name in file_names:
    input_path = os.path.join(data_dir, file_name)
    df = pd.read_csv(input_path)
    df.columns = clean_column_names(df.columns)

    # Clean filename
    cleaned_name = file_name.replace('-', '_').replace(' ', '_').replace('%', 'percent').lower()
    cleaned_name = cleaned_name.replace('__', '_')

    # Save cleaned CSV
    output_path = os.path.join(seeds_dir, cleaned_name)
    df.to_csv(output_path, index=False)
    print(f"Saved cleaned file: {output_path}")
