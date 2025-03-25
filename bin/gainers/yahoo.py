import os
import pandas as pd
import sys
from datetime import datetime

class GainerDownloadYahoo:
    def __init__(self):
        self.url = "https://finance.yahoo.com/markets/stocks/gainers/?start=0&count=200"

    def download(self):
	"""
	Download Yahoo ygainers data.
	"""
        print("Downloading Yahoo gainers")
        download_command = "sudo google-chrome-stable --headless --disable-gpu --dump-dom --no-sandbox --timeout=5000 '" + self.url + "' > ../scripts/ygainers.html"
        exit_code = os.system(download_command)
        if exit_code != 0:
            print("Error: Failed to download Yahoo gainers HTML file.")
            return  # Exit if the download fails

        print("Downloaded Yahoo HTML file, converting to CSV...")
        convert_command = "python -c 'import pandas as pd; raw = pd.read_html(\"../scripts/ygainers.html\")[0]; raw.to_csv(\"../sample_data/ygainers.csv\")'"
        exit_code = os.system(convert_command)
        if exit_code != 0:
            print("Error: Failed to convert Yahoo HTML to CSV.")
            return  # Exit if the conversion fails

        print("Yahoo gainer data converted to ygainers.csv and saved in ../sample_data")

class GainerProcessYahoo:
    def __init__(self, input_path='../scripts/ygainers.html', output_path='../sample_data/ygainers.csv'):
        self.input_path = input_path
        self.output_path = output_path

    def normalize(self):
	"""
	Normalize the WSJ gainer data from CSV.
	"""
        try:
            print("Normalizing Yahoo gainers")
            ygainers = pd.read_csv(self.input_path)
            ygainers = ygainers[['Symbol', 'Name', 'Last Price', 'Change', '% Change']]
            ygainers = ygainers.rename(columns={
                'Symbol': 'symbol',
                'Name': 'name',
                'Last Price': 'price',
                'Change': 'price_change',
                '% Change': 'price_percent_change'
            })
            ygainers.dropna(inplace=True)
            ygainers = ygainers.astype({'symbol': 'str', 'name': 'str', 'price': 'float', 'price_change': 'float', 'price_percent_change': 'float'})
            self.save_with_timestamp(ygainers)
            print(f"Normalization complete. Data saved to {self.output_path}")
        except AssertionError as e:
            print(f"Assertion Error: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def save_with_timestamp(self, ygainers):
        """
        Save the normalized csv with a timestamp in the filename.
        """
        current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"ygainers_{current_time}.csv"
        full_path = os.path.join(os.path.dirname(self.output_path), filename)
        ygainers.to_csv(full_path, index=False)
        print(f"Saved normalized data with timestamp: {full_path}")

if __name__ == "__main__":
    processor = GainerProcessYahoo()
    processor.normalize()
