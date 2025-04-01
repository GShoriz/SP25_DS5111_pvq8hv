"""
Factory Module to direct calls to specific gainers.
"""
from yahoo import GainerDownloadYahoo, GainerProcessYahoo
from wsj import GainerDownloadWSJ, GainerProcessWSJ
from sanalysis import GainerDownloadSANALYSIS, GainerProcessSANALYSIS

class GainerFactory:
    """
    Factory class to instantiate downloader and processor objects for various sources.
    """
    def __init__(self, choice):
        """
        Initializes the factory with the specified choice of gainer type.
        """
        assert choice in ['yahoo', 'wsj', 'sanalysis', 'test'], f"Unrecognized gainer type {choice}"
        self.choice = choice

    def get_downloader(self):
        """
        Returns an instance of the appropriate downloader based on the chosen source.
        """
        if self.choice == 'yahoo':
            return GainerDownloadYahoo()
        if self.choice == 'wsj':
            return GainerDownloadWSJ()
        if self.choice == 'sanalysis':
            return GainerDownloadSANALYSIS()
        raise ValueError(f"Unrecognized gainer type: {self.choice}")

    def get_processor(self):
        """
        Returns an instance of the appropriate processor based on the chosen source.
        """
        if self.choice == 'yahoo':
            return GainerProcessYahoo()
        if self.choice == 'wsj':
            return GainerProcessWSJ()
        if self.choice == 'sanalysis':
            return GainerProcessSANALYSIS()
        raise ValueError(f"Unrecognized gainer type: {self.choice}")
