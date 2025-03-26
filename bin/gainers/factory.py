"""
Factory Module to direct calls to specific gainers.
"""
from yahoo import GainerDownloadYahoo, GainerProcessYahoo
from wsj import GainerDownloadWSJ, GainerProcessWSJ
from cnbc import GainerDownloadCNBC, GainerProcessCNBC

class GainerFactory:
    """
    Factory class to instantiate downloader and processor objects for various sources.
    """
    def __init__(self, choice):
        """
        Initializes the factory with the specified choice of gainer type.
        """
        assert choice in ['yahoo', 'wsj', 'cnbc', 'test'], f"Unrecognized gainer type {choice}"
        self.choice = choice

    def get_downloader(self):
        """
        Returns an instance of the appropriate downloader based on the chosen source.
        """
        if self.choice == 'yahoo':
            return GainerDownloadYahoo()
        elif self.choice == 'wsj':
            return GainerDownloadWSJ()
        elif self.choice == 'cnbc':
            return GainerDownloadCNBC()
        raise ValueError(f"Unrecognized gainer type: {self.choice}")

    def get_processor(self):
        """
        Returns an instance of the appropriate processor based on the chosen source.
        """
        if self.choice == 'yahoo':
            return GainerProcessYahoo()
        elif self.choice == 'wsj':
            return GainerProcessWSJ()
        elif self.choice == 'cnbc':
            return GainerProcessCNBC()
        raise ValueError(f"Unrecognized gainer type: {self.choice}")
