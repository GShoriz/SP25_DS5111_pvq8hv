import os
import pandas as pd
import sys

class GainerDownloadWSJ(GainerDownload):
	def __init__(self):
		super().__init__("https://www.wsj.com/market-data/stocks/us/movers")

	def download(self):
		print("Downloading WSJ gainers")

	download_command = """sudo google-chrome-stable --headless --disable-gpu --dump-dom --no-sandbox --timeout=5000 \
        'https://www.wsj.com/market-data/stocks/us/movers' > ../scripts/wsjgainers.html"""

	exit_code = os.system(command)
	if exit_code != 0:
		print("Error: Failed to download WSJ gainers HTML file.")

	return
		print("Downloaded WSJ HTML file, converting to CSV...")

	convert_command = """python -c 'import pandas as pd; \
        raw = pd.read_html("../scripts/wsjgainers.html"); raw[0].to_csv("../sample_data/wsjgainers.csv")'"""

	exit_code = os.system(convert_command)
	if exit_code != 0:
		print("Error: Failed to convert WSJ HTML to CSV.")

	return
		print("WSJ gainer data converted to wsjgainer.csv")

class GainerProcessWSJ
	def __init__(self, input_path='../scripts/wsjgainer.html', output_path='../sample_data/wsjgainers.csv':
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


            wsjgainers = wsjgainers[['Unnamed: 0', 'Last', 'Chg', '% Chg']]
            wsjgainers = wsjgainers.rename(columns={
                'Unnamed: 0': 'symbol',
                'Last': 'price',
                'Chg': 'price_change',
                '% Chg': 'price_percent_change'
            })
            wsjgainers['symbol'] = wsjgainers['symbol'].str.extract(r'\((\w+)\)')


            wsjgainers = wsjgainers.dropna().astype({
                'symbol': 'str',
                'price': 'float',
                'price_change': 'float',
                'price_percent_change': 'float'
            })
            assert wsjgainers.shape[1] == 4, "Expected 4 columns after transformation"


            wsjgainers.to_csv(self.output_path, index=False)
            print(f"Normalization complete. Data saved to {self.output_path}")

        except AssertionError as e:
            print(f"Assertion Error: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    processor = GainerProcessWSJ()
    processor.normalize()
