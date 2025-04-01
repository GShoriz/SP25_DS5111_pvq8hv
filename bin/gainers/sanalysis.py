"""
This module provides classes for downloading and processing Stock Analysis gainer data.
"""

import os
from datetime import datetime
import pandas as pd
from base import GainerDownload, GainerProcess

class GainerDownloadSANALYSIS(GainerDownload): # pylint: disable=too-few-public-methods
    """
    Handles the downloading of Stock Analysis gainer data.
    """
    def __init__(self):
        super().__init__()
        self.url = "https://stockanalysis.com/markets/gainers/"

    def download(self):
        """
        Download Stock Analysis data, convert to CSV, and handle errors.
        """
        print("Downloading Stock Analysis gainers")
        download_command = (
            "sudo google-chrome-stable --headless --disable-gpu --dump-dom "
            "--no-sandbox --timeout=5000 '" + self.url + "' > ../scripts/sanalysis.html"
        )
        if os.system(download_command) != 0:
            print("Error: Failed to download sanalysis gainers HTML file.")
            return

        print("Downloaded Stock Analysis HTML file, converting to CSV...")
        convert_command = ("python -c 'import pandas as pd; "
                           "raw = pd.read_html(\"../scripts/sanalysisgainers.html\")[0]; "
                           "raw.to_csv(\"../sample_data/sanalysisgainers.csv\")'")
        if os.system(convert_command) != 0:
            print("Error: Failed to convert Stock Analysis HTML to CSV.")
            return

        print("Stock Analysis gainer data converted to sanalysisgainers.csv and saved in ../sample_data")
class GainerProcessSANALYSIS(GainerProcess):
    """
    Handles normalization and timestamped saving of Stock Analysis gainer data.
    """
    def __init__(self,
                 input_path='../scripts/sanalysisgainers.html',
                 output_path='../sample_data/sanalysisgainers.csv'):
        self.input_path = input_path
        self.output_path = output_path

    def normalize(self):
        """
        Normalize the Stock Analysis gainer data from CSV.
        """
        try:
            print("Normalizing Stock Analysis gainers")
            sanalysisgainers = pd.read_csv(self.input_path)
            assert sanalysisgainers.shape[1] == 6, "Expected 6 columns in the input CSV"
            sanalysisgainers = sanalysisgainers[['Unnamed: 0', 'Last', 'Chg', '% Chg']].rename(
                columns={
                    'Unnamed: 0': 'symbol',
                    'Last': 'price',
                    'Chg': 'price_change',
                    '% Chg': 'price_percent_change'
                }
            )
            sanalysisgainers['symbol'] = sanalysisgainers['symbol'].str.extract(r'\((\w+)\)')
            sanalysisgainers.dropna(inplace=True)
            sanalysisgainers = sanalysisgainers.astype({
                'symbol': 'str',
                'price': 'float',
                'price_change': 'float',
                'price_percent_change': 'float'
            })
            assert sanalysisgainers.shape[1] == 4, "Expected 4 columns after transformation"
            self.save_with_timestamp(sanalysisgainers)
        except AssertionError as error:
            print(f"Assertion Error: {error}")
        except Exception as error: # pylint: disable=broad-except
            print(f"An error occurred: {error}")

    def save_with_timestamp(self, data):
        """
        Save the normalized csv with a timestamp in the filename.
        """
        current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"sanalysisgainers_{current_time}.csv"
        full_path = os.path.join(os.path.dirname(self.output_path), filename)
        data.to_csv(full_path, index=False)
        print(f"Saved normalized data with timestamp: {full_path}")

if __name__ == "__main__":
    processor = GainerProcessSANALYSIS()
    processor.normalize()
