from abc import ABC, abstractmethod
from base import GainerDownload, GainerProcess

class GainerFactory:
	def __init__(self, choice):
		assert choice in ['yahoo', 'wsj','cnbc', 'test'], f"Unrecognized gainer type {choice}"
		self.choice = choice

	def get _downloader(self):
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
