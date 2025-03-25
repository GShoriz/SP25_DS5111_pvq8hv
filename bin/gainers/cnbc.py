import os
import pandas as pd
from datetime import datetime

class GainerDownloadCNBC:
    def __init__(self):
        self.url = "https://www.cnbc.com/us-market-movers/"
	"""
	Downloads data from CNBC.
	"""
    def download(self):
        print("Downloading CNBC gainers")
        download_command = "sudo google-chrome-stable --headless --disable-gpu --dump-dom --no-sandbox --timeout=5000 '" + self.url + "' > ../scripts/cnbcgainers.html"
        exit_code = os.system(download_command)
        if exit_code != 0:
            print("Error: Failed to download CNBC gainers HTML file.")
            return  # Exit if the download fails

        print("Downloaded CNBC HTML file, converting to CSV...")
        convert_command = "python -c 'import pandas as pd; raw = pd.read_html(\"../scripts/cnbcgainers.html\")[0]; raw.to_csv(\"../sample_data/cnbcgainers.csv\")'"
        exit_code = os.system(convert_command)
        if exit_code != 0:
            print("Error: Failed to convert CNBC HTML to CSV.")
            return  # Exit if the conversion fails

        print("CNBC gainer data converted to cnbcgainers.csv and saved in ../sample_data")

class GainerProcessCNBC:
    def __init__(self, input_path='../scripts/cnbcgainers.html', output_path='../sample_data/cnbcgainers.csv'):
        self.input_path = input_path
        self.output_path = output_path

    def normalize(self):
	"""
	Normalize the cnbc gainer data from CSV.
	"""

        try:
            print("Normalizing CNBC gainers")
            cnbcgainers = pd.read_csv(self.input_path)
            # Assuming the column headers - these will need to be adjusted according to actual data
            cnbcgainers = cnbcgainers[['Symbol', 'Company Name', 'Price', 'Change', '% Change']]
            cnbcgainers = cnbcgainers.rename(columns={
                'Symbol': 'symbol',
                'Company Name': 'name',
                'Price': 'price',
                'Change': 'price_change',
                '% Change': 'price_percent_change'
            })
            cnbcgainers.dropna(inplace=True)
            cnbcgainers = cnbcgainers.astype({'symbol': 'str', 'name': 'str', 'price': 'float', 'price_change': 'float', 'price_percent_change': 'float'})
            self.save_with_timestamp(cnbcgainers)
            print(f"Normalization complete. Data saved to {self.output_path}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def save_with_timestamp(self, cnbcgainers):
        """
        Save the normalized csv with a timestamp in the filename.
        """
        current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"cnbcgainers_{current_time}.csv"
        full_path = os.path.join(os.path.dirname(self.output_path), filename)
        cnbcgainers.to_csv(full_path, index=False)
        print(f"Saved normalized data with timestamp: {full_path}")

if __name__ == "__main__":
    processor = GainerProcessCNBC()
    processor.normalize()
