"""
This module provides classes for downloading and processing WSJ gainer data.
"""

import os
from datetime import datetime
import pandas as pd
from bin.gainers.base import GainerDownlaod
from bin.gainers.base import GainerProcess

class GainerDownloadWSJ(GainerDownlaod):
    """
    Handles the downloading of WSJ gainer data.
    """
    def __init__(self):
        self.url = "https://www.wsj.com/market-data/stocks/us/movers"

    def download(self):
        """
        Download WSJ data, convert to CSV, and handle errors.
        """
        print("Downloading WSJ gainers")
        download_command = ("sudo google-chrome-stable --headless --disable-gpu --dump-dom --no-sandbox --timeout=5000 "
                            f"'{self.url}' > ../scripts/wsjgainers.html")
        if os.system(download_command) != 0:
            print("Error: Failed to download WSJ gainers HTML file.")
            return

        print("Downloaded WSJ HTML file, converting to CSV...")
        convert_command = ("python -c 'import pandas as pd; "
                           "raw = pd.read_html(\"../scripts/wsjgainers.html\")[0]; "
                           "raw.to_csv(\"../sample_data/wsjgainers.csv\")'")
        if os.system(convert_command) != 0:
            print("Error: Failed to convert WSJ HTML to CSV.")
            return

        print("WSJ gainer data converted to wsjgainers.csv and saved in ../sample_data")

class GainerProcessWSJ(GainerProcess):
    """
    Handles normalization and timestamped saving of WSJ gainer data.
    """
    def __init__(self,
                 input_path='../scripts/wsjgainers.html',
                 output_path='../sample_data/wsjgainers.csv'):
        self.input_path = input_path
        self.output_path = output_path

    def normalize(self):
        """
        Normalize the WSJ gainer data from CSV.
        """
        try:
            print("Normalizing WSJ gainers")
            wsjgainers = pd.read_csv(self.input_path)
            assert wsjgainers.shape[1] == 6, "Expected 6 columns in the input CSV"
            wsjgainers = wsjgainers[['Unnamed: 0', 'Last', 'Chg', '% Chg']].rename(
                columns={
                    'Unnamed: 0': 'symbol',
                    'Last': 'price',
                    'Chg': 'price_change',
                    '% Chg': 'price_percent_change'
                }
            )
            wsjgainers['symbol'] = wsjgainers['symbol'].str.extract(r'\((\w+)\)')
            wsjgainers.dropna(inplace=True)
            wsjgainers = wsjgainers.astype({
                'symbol': 'str',
                'price': 'float',
                'price_change': 'float',
                'price_percent_change': 'float'
            })
            assert wsjgainers.shape[1] == 4, "Expected 4 columns after transformation"
            self.save_with_timestamp(wsjgainers)
        except AssertionError as error:
            print(f"Assertion Error: {error}")
        except Exception as error:
            print(f"An error occurred: {error}")

    def save_with_timestamp(self, wsjgainers):
        """
        Save the normalized csv with a timestamp in the filename.
        """
        current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"wsjgainers_{current_time}.csv"
        full_path = os.path.join(os.path.dirname(self.output_path), filename)
        wsjgainers.to_csv(full_path, index=False)
        print(f"Saved normalized data with timestamp: {full_path}")

if __name__ == "__main__":
    processor = GainerProcessWSJ()
    processor.normalize()
