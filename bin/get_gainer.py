"""
Main script to process different types of gainers.
"""

import sys
from bin.gainers.factory import GainerFactory

class ProcessGainer: # pylint: disable=too-few-public-methods
    """
    Orchestrates the downloading, normalization, and saving of gainer data.
    """
    def __init__(self, gainer_downloader, gainer_normalizer):
        self.downloader = gainer_downloader
        self.normalizer = gainer_normalizer

    def _download(self):
        """
        Download the data using the specified downloader.
        """
        self.downloader.download()

    def _normalize(self):
        """
        Normalize the data using the specified normalizer.
        """
        self.normalizer.normalize()

    def _save_to_file(self):
        """
        Save the normalized data with a timestamp using the normalizer's method.
        """
        self.normalizer.save_with_timestamp()

    def process(self):
        """
        Execute the download, normalization, and saving processes in sequence.
        """
        self._download()
        self._normalize()
        self._save_to_file()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python get_gainer.py <gainer_type>")
        print("gainer_type options: 'yahoo', 'wsj', 'cnbc', 'test'")
        sys.exit(1)

    choice = sys.argv[1]
    factory = GainerFactory(choice)
    downloader = factory.get_downloader()
    normalizer = factory.get_processor()

    runner = ProcessGainer(downloader, normalizer)
    runner.process()
