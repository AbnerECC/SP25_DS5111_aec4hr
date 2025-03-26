from abc import ABCMeta, abstractmethod

# Abstract Classes for Downloaders and Processers

class GainerDownload(metaclass = ABCMeta):
    
    @abstractmethod
    def download(self):
        pass


class GainerProcess(metaclass = ABCMeta):
    
    def normalize(self):
        pass

    def save_with_timestamp(self):
      pass

# Concrete Class for Gainers Download

class GainerDownloadYahoo(GainerDownload):
    
    def download(self):
        print("Downloading Yahoo gainers")

class GainerDownloadWSJ(GainerDownload):
    
    def download(self):
        print("Downloading WSJ gainers")

# Concrete Classes for Gainer Processors

class GainerProcessYahoo(GainerProcess):
    
    def normalize(self):
        print("Normalizing Yahoo gainers")

    def save_with_timestamp(self):
        print("Saving Yahoo gainers")

class GainerProcessWSJ(GainerProcess):
    
    def normalize(self):
        print("Normalizing WSJ gainers")

    def save_with_timestamp(self):
        print("Saving WSJ gainers")
 



## Factory Class to Create Correct Downloader and Processor Based on Input

class GainerFactory(object):
    
    def __init__(self):
        # Mapping of animal type to their respective classes
        self.downloaders = {
            'yahoo': GainerDownloadYahoo,
            'wsj': GainerDownloadWSJ
        }

        self.processors = {
            'yahoo': GainerProcessYahoo,
            'wsj': GainerProcessWSJ
        }

    def make_downloader(self, object_type: str) -> GainerDownload:
        """Return the correct downloader class based on input type."""
        downloader_class = self.downloaders.get(object_type)
        if downloader_class:
            return downloader_class()
        else:
            print(f"Invalid gainer type for downloader: {object_type}")
            return None

    def make_processor(self, object_type: str) -> GainerProcess:
        """Return the correct processor class based on input type."""
        processor_class = self.processors.get(object_type)
        if processor_class:
            return processor_class()
        else:
            print(f"Invalid gainer type for processor: {object_type}")
            return None


## Client Code

if __name__ == '__main__':
    factory = GainerFactory()

    # Input from user for which gainer to process
    gainer_type = input("Which gainer would you like to process? (yahoo or wsj): ").strip()

    # Create the downloader and processor for the selected gainer type
    downloader = factory.make_downloader(gainer_type)
    processor = factory.make_processor(gainer_type)

    if downloader and processor:
        # Run the download, normalize, and save steps
        downloader.download()
        processor.normalize()
        processor.save_with_timestamp()