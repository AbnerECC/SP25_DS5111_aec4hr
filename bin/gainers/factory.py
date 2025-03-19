"""Factory Module for the Gainer selection"""
#from abc import ABC, abstractmethod

# FACTORY
class GainerFactory:
    """Factory to create appropriate download and processer based on source."""
    def __init__(self, choice):
        assert choice in ['yahoo', 'wsj', 'test'], f"Unrecognized gainer type {choice}"
        self.choice = choice

    def get_downloader(self):
        """Get the user input for the downloader to use"""
        # trigger off url to return correct downloader
        if self.choice == 'yahoo':
            return GainerDownloadYahoo()
        if self.choice == 'wsj':
            return GainerDownloadWSJ()

    def get_processor(self):
        """Get the user input for the processer to use"""
        # trigger off url to return correct downloader
        if self.choice == 'yahoo':
            return GainerProcessYahoo()
        if self.choice == 'wsj':
            return GainerProcessWSJ()
