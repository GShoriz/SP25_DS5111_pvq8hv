"""
This module provides classes for downloading and processing Yahoo gainer data.
"""

import os
from datetime import datetime
import pandas as pd
from base import GainerDownload, GainerProcess

class GainerDownloadYahoo(GainerDownload): # pylint: disable=too-few-public-methods
    """
    Handles the downloading of WSJ gainer data.
    """
    def __init__(self):
        super().__init__()
        self.url = "https://finance.yahoo.com/markets/stocks/gainers/?start=0&count=200"

    def download(self):
        """
        Download Yahoo data, convert to CSV, and handle errors.
        """
        print("Downloading Yahoo gainers")
        download_command = (
            "sudo google-chrome-stable --headless --disable-gpu --dump-dom "
            "--no-sandbox --timeout=5000 '" + self.url + "' > ../scripts/yahoogainers.html"
        )
        if os.system(download_command) != 0:
            print("Error: Failed to download Yahoo gainers HTML file.")
            return

        print("Downloaded Yahoo HTML file, converting to CSV...")
        convert_command = ("python -c 'import pandas as pd; "
                           "raw = pd.read_html(\"../scripts/yahoogainers.html\")[0]; "
                           "raw.to_csv(\"../sample_data/yahoogainers.csv\")'")
        if os.system(convert_command) != 0:
            print("Error: Failed to convert yahoo HTML to CSV.")
            return

        print("Yahoo gainer data converted to wsjgainers.csv and saved in ../sample_data")
class GainerProcessYahoo(GainerProcess):
    """
    Handles normalization and timestamped saving of Yahoo gainer data.
    """
    def __init__(self,
                 input_path='../scripts/yahoogainers.html',
                 output_path='../sample_data/yahoogainers.csv'):
        self.input_path = input_path
        self.output_path = output_path

    def normalize(self):
        """
        Normalize the Yahoo gainer data from CSV.
        """
        try:
            print("Normalizing Yahoo gainers")
            yahoogainers = pd.read_csv(self.input_path)
            assert yahoogainers.shape[1] == 6, "Expected 6 columns in the input CSV"
            yahoogainers = yahoogainers[['Unnamed: 0', 'Last', 'Chg', '% Chg']].rename(
                columns={
                    'Unnamed: 0': 'symbol',
                    'Last': 'price',
                    'Chg': 'price_change',
                    '% Chg': 'price_percent_change'
                }
            )
            yahoogainers['symbol'] = yahoogainers['symbol'].str.extract(r'\((\w+)\)')
            yahoogainers.dropna(inplace=True)
            yahoogainers = yahoogainers.astype({
                'symbol': 'str',
                'price': 'float',
                'price_change': 'float',
                'price_percent_change': 'float'
            })
            assert yahoogainers.shape[1] == 4, "Expected 4 columns after transformation"
            self.save_with_timestamp(yahoogainers)
        except AssertionError as error:
            print(f"Assertion Error: {error}")
        except Exception as error: # pylint: disable=broad-except
            print(f"An error occurred: {error}")

    def save_with_timestamp(self, data):
        """
        Save the normalized csv with a timestamp in the filename.
        """
        current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"yahoogainers_{current_time}.csv"
        full_path = os.path.join(os.path.dirname(self.output_path), filename)
        data.to_csv(full_path, index=False)
        print(f"Saved normalized data with timestamp: {full_path}")

if __name__ == "__main__":
    processor = GainerProcessYahoo()
    processor.normalize()
