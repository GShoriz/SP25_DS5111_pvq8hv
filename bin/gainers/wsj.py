import os

class GainerDownloadWSJ(GainerDownload):
	def __init__(self):
		super().__init__("https://www.wsj.com/market-data/stocks/us/movers")

	def download(self):
		print("Downloading WSJ gainers")

	command = """sudo google-chrome-stable --headless --disable-gpu --dump-dom --no-sandbox --timeout=5000 \
        'https://www.wsj.com/market-data/stocks/us/movers' > wsjgainers.html"""

	exit_code = os.system(command)
	if exit_code != 0:
		print("Error: Failed to download WSJ gainers HTML file.")

	return
		print("Downloaded WSJ HTML file, converting to CSV...")

	convert_command = """python -c 'import pandas as pd; \
        raw = pd.read_html("wsjgainers.html"); raw[0].to_csv("wsjgainers.csv")'"""

	exit_code = os.system(convert_command)
	if exit_code != 0:
		print("Error: Failed to convert WSJ HTML to CSV.")

	return
		print("WSJ gainer data converted to wsjgainer.csv")

