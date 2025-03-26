"""Module for processing stock gainer data"""

from abc import ABC, abstractmethod

#DOWNLOADER
class GainerDownload(ABC):
    """Abstract Class for downloading Stock gainer data."""
    def __init__(self, url=None):
        self.url = url

    @abstractmethod
    def download(self):
        """Abstract Download Method"""
        pass

#PROCESSORS
class GainerProcess(ABC):
    """Abstract class for processing stock gainer data."""
    def __init__(self):
        pass

    @abstractmethod
    def normalize(self):
        """Abstract normalizing method."""
        pass

    @abstractmethod
    def save_with_timestamp(self):
        """Abstract saving timestamp method"""
        pass

class ProcessGainer:
    """Template class for the process gainer"""
    def __init__(self, gainer_downloader, gainer_normalizer):
        self.downloader = gainer_downloader
        self.normalizer = gainer_normalizer

    def _download(self):
        self.downloader.download()

    def _normalize(self):
        self.normalizer.normalize()

    def _save_to_file(self):
        self.normalizer.save_with_timestamp()

    def process(self):
        """Running the full created workflow for the gainer file"""
        self._download()
        self._normalize()
        self._save_to_file()