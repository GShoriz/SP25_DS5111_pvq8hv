from base import GainerDownload, GainerProcess
from yahoo import GainerDownloadYahoo, GainerProcessYahoo
from wsj import GainerDownloadWSJ, GainerProcessWSJ
from cnbc import GainerDownloadCNBC, GainerProcessCNBC

class GainerFactory:
	def __init__(self, choice):
		assert choice in ['yahoo', 'wsj', 'cnbc', 'test'], f"Unrecognized gainer type {choice}"
		self.choice = choice

	def get_downloader(self):
		if self.choice == 'yahoo':
			return GainerDownloadYahoo()
		elif self.choice == 'wsj':
			return GainerDownloadWSJ()
		elif self.choice == 'cnbc':
			return GainerDownloadCNBC()

	def get_processor(self):
		if self.choice == 'yahoo':
			return GainerProcessYahoo()
		elif self.choice == 'wsj':
			return GainerProcessWSJ()
		elif self.choice == 'cnbc':
			return GainerProcessCNBC()
