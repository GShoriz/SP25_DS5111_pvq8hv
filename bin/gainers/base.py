"""
This module defines abstract base classes for downloading and processing gainer data.
"""

from abc import ABC, abstractmethod

class GainerDownload(ABC):  # pylint: disable=too-few-public-methods, unnecessary-pass
    """
    Abstract base class for downloading gainers.
    Provides a template for downloading operations.
    """

    def __init__(self, url=None):
        """
        Initialize the downloader with a URL if provided.
        """
        self.url = url

    @abstractmethod
    def download(self):
        """
        Abstract method to download data. Must be implemented by subclasses.
        """
        # pass

class GainerProcess(ABC):  # pylint: disable=too-few-public-methods, unnecessary-pass
    """
    Abstract base class for processing gainers.
    Provides a template for data processing operations.
    """

    @abstractmethod
    def normalize(self):
        """
        Abstract method to normalize the data. Must be implemented by subclasses.
        """
        # pass

    @abstractmethod
    def save_with_timestamp(self, data):
        """
        Abstract method to save data with a timestamp. Must be implemented by subclasses.
        """
        # pass
