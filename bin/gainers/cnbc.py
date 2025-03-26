"""
This module provides classes for downloading and processing CNBC gainer data.
"""

import os
from datetime import datetime
import pandas as pd
from base import GainerDownload, GainerProcess

class GainerDownloadCNBC(GainerDownload): # pylint: disable=too-few-public-methods
    """
    Handles the downloading of WSJ gainer data.
    """
    def __init__(self):
        super().__init__()
        self.url = "https://www.cnbc.com/us-market-movers/"

    def download(self):
        """
        Download CNBC data, convert to CSV, and handle errors.
        """
        print("Downloading CNBC gainers")
        download_command = (
            "sudo google-chrome-stable --headless --disable-gpu --dump-dom "
            "--no-sandbox --timeout=5000 '" + self.url + "' > ../scripts/cnbcgainers.html"
        )
        if os.system(download_command) != 0:
            print("Error: Failed to download CNBC gainers HTML file.")
            return

        print("Downloaded CNBC HTML file, converting to CSV...")
        convert_command = ("python -c 'import pandas as pd; "
                           "raw = pd.read_html(\"../scripts/cnbcgainers.html\")[0]; "
                           "raw.to_csv(\"../sample_data/cnbcgainers.csv\")'")
        if os.system(convert_command) != 0:
            print("Error: Failed to convert CNBC HTML to CSV.")
            return

        print("CNBC gainer data converted to cnbcgainers.csv and saved in ../sample_data")
class GainerProcessCNBC(GainerProcess):
    """
    Handles normalization and timestamped saving of CNBC gainer data.
    """
    def __init__(self,
                 input_path='../scripts/cnbcgainers.html',
                 output_path='../sample_data/cnbcgainers.csv'):
        self.input_path = input_path
        self.output_path = output_path

    def normalize(self):
        """
        Normalize the CNBC gainer data from CSV.
        """
        try:
            print("Normalizing CNBC gainers")
            cnbcgainers = pd.read_csv(self.input_path)
            assert cnbcgainers.shape[1] == 6, "Expected 6 columns in the input CSV"
            cnbcgainers = cnbcgainers[['Unnamed: 0', 'Last', 'Chg', '% Chg']].rename(
                columns={
                    'Unnamed: 0': 'symbol',
                    'Last': 'price',
                    'Chg': 'price_change',
                    '% Chg': 'price_percent_change'
                }
            )
            cnbcgainers['symbol'] = cnbcgainers['symbol'].str.extract(r'\((\w+)\)')
            cnbcgainers.dropna(inplace=True)
            cnbcgainers = cnbcgainers.astype({
                'symbol': 'str',
                'price': 'float',
                'price_change': 'float',
                'price_percent_change': 'float'
            })
            assert cnbcgainers.shape[1] == 4, "Expected 4 columns after transformation"
            self.save_with_timestamp(cnbcgainers)
        except AssertionError as error:
            print(f"Assertion Error: {error}")
        except Exception as error: # pylint: disable=broad-except
            print(f"An error occurred: {error}")

    def save_with_timestamp(self, data):
        """
        Save the normalized csv with a timestamp in the filename.
        """
        current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"cnbcgainers_{current_time}.csv"
        full_path = os.path.join(os.path.dirname(self.output_path), filename)
        data.to_csv(full_path, index=False)
        print(f"Saved normalized data with timestamp: {full_path}")

if __name__ == "__main__":
    processor = GainerProcessCNBC()
    processor.normalize()
