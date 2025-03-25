from abc import ABC, abstractmethod

class GainerDownload(ABC):
    """
    Abstract base class for downloading gainers.
    """

    def __init__(self, url=None):
        """
        Initialize the downloader with a URL.
        """
        self.url = url

    @abstractmethod
    def download(self):
        """
        Method to download data. Must be implemented by subclasses.
        """
        pass

class GainerProcess(ABC):
    """
    Abstract base class for processing gainers.
    """

    @abstractmethod
    def normalize(self):
        """
        Method to normalize the data. Must be implemented by subclasses.
        """
        pass

    @abstractmethod
    def save_with_timestamp(self, data):
        """
        Method to save data with a timestamp. Must be implemented by subclasses.
        """
        pass
