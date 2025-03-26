import sys
sys.path.append('/home/ubuntu/SP25_DS5111_aec4hr/bin/gainers/')
from factory import GainerFactory
from wsj import GainerDownloadWSJ, GainerProcessWSJ
from yahoo import GainerDownloadYahoo, GainerProcessYahoo

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

if __name__=="__main__":
   
    # Make our selection, 'one' choice
    choice = sys.argv[1]

    # let our factory get select the family of objects for processing
    factory = GainerFactory(choice)
    downloader = factory.get_downloader()
    normalizer = factory.get_processor()

    # create our process
    runner = ProcessGainer(downloader, normalizer)
    runner.process()