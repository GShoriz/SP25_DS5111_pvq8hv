"""
Module provides a factory class to create downloader and processor objects based on a given source.
"""

from base import GainerDownload, GainerProcess
from yahoo import GainerDownloadYahoo, GainerProcessYahoo
from wsj import GainerDownloadWSJ, GainerProcessWSJ
from cnbc import GainerDownloadCNBC, GainerProcessCNBC

class GainerFactory:
	"""
	Factory class to instantiate downloader and processor objects for various sources.
	"""
	def __init__(self, choice):
		assert choice in ['yahoo', 'wsj', 'cnbc', 'test'], f"Unrecognized gainer type {choice}"
		self.choice = choice

	def get_downloader(self):
		"""
		Returns an instance of the appropriate downloader based on the chosen source.
		"""
		if self.choice == 'yahoo':
			return GainerDownloadYahoo()
		if self.choice == 'wsj':
			return GainerDownloadWSJ()
		if self.choice == 'cnbc':
			return GainerDownloadCNBC()

	def get_processor(self):
		"""
		Returns an instance of the appropriate processor based on the chosen source.
		"""
		if self.choice == 'yahoo':
			return GainerProcessYahoo()
		if self.choice == 'wsj':
			return GainerProcessWSJ()
		if self.choice == 'cnbc':
			return GainerProcessCNBC()
