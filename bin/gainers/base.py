"""Module for processing stock gainer data"""

from abc import ABC, abstractmethod
import sys
import pandas as pd


# FACTORY
# class GainerFactory:
    # """Factory to create appropriate download and processer based on source."""
    # def __init__(self, choice):
        # assert choice in ['yahoo', 'wsj', 'test'], f"Unrecognized gainer type {choice}"
        # self.choice = choice

    # def get_downloader(self):
        # """Get the user input for the downloader to use"""
        # # trigger off url to return correct downloader
        # if self.choice == 'yahoo':
            # return GainerDownloadYahoo()
        # if self.choice == 'wsj':
            # return GainerDownloadWSJ()

    # def get_processor(self):
        # """Get the user input for the processer to use"""
        # # trigger off url to return correct downloader
        # if self.choice == 'yahoo':
            # return GainerProcessYahoo()
        # if self.choice == 'wsj':
            # return GainerProcessWSJ()

#DOWNLOADER
class GainerDownload(ABC):
    """Abstract Class for downloading Stock gainer data."""
    def __init__(self, url=None):
        self.url = url

    @abstractmethod
    def download(self):
        """Abstract Download Method"""
        pass

# class GainerDownloadYahoo(GainerDownload):
    # """Class to download the gainer data from yahoo."""
    # def __init__(self):
        # super().__init__('~/SP25_DS5111_aec4hr/ygainers.html') #Enter the default URL here
        # #pass

    # def download(self):
        # """Downloads gainer data from the specified source."""
        # raw = pd.read_html(self.url)
        # raw[0].to_csv('ygainers.csv')
        # print("Downloading yahoo gainers")
        # return raw

# class GainerDownloadWSJ(GainerDownload):
    # """Class to download the gainer data from WSJ."""
    # def __init__(self):
        # super().__init__('~/SP25_DS5111_aec4hr/wsjgainers.html')
        # #pass

    # def download(self):
        # """Downloads gainer data from the specified source."""
        # raw = pd.read_html(self.url)
        # raw[0].to_csv('wsjgainers.csv')
        # print("Downloading WSJ gainers")
        # return raw

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

# class GainerProcessYahoo(GainerProcess):
    # """Class for processing the gainer data from yahoo."""
    # def __init__(self, csv_path=None):
        # self.csv_path = csv_path if csv_path else 'ygainers.csv'
        # #pass

    # def normalize(self):
        # """Normalizers the yahoo gainer data into the correct format."""
        # assert self.csv_path.endswith('.csv'),\
        # f'The file path {self.csv_path} does not end with a .csv'

        # output = pd.read_csv(self.csv_path, usecols=['Symbol','Price', 'Change', 'Change %'])

        # output = output.rename(
            # columns={'Symbol':'symbol',
             # 'Price':'price',
              # 'Change':'price_change',
               # 'Change %':'price_percent_change'})

        # expected_cols = ['symbol', 'price', 'price_change', 'price_percent_change']

        # assert len(output.columns) == 4, f'Expected column length 4 but got {len(output.columns)}'

        # assert output.columns.values.tolist() == list(expected_cols),\
         # f'Expected column names of {expected_cols} but got {output.columns}'

        # output['price'] = output['price'].str.split('+', n=1).str[0]

        # print("Normalizing yahoo gainers")
        # return output


    # def save_with_timestamp(self):
        # """Saves the yahoo dataset with the current timestamp."""
        # output = self.normalize()
        # timestamp = pd.to_datetime('now').strftime('%Y%m%d_%H%M%S')
        # out_path = f'ygainers_norm_{timestamp}.csv'
        # output.to_csv(out_path)
        # ##out_path  = '~/SP25_DS5111_aec4hr/ygainers_norm.csv'
        # print("Saving Yahoo gainers")

# # ITS OWN SEPARATE FILE
# class GainerProcessWSJ(GainerProcess):
    # """Class for processing the gainer data from WSJ."""
    # def __init__(self, csv_path=None):
        # self.csv_path = csv_path if csv_path else 'wsjgainers.csv'
        # #pass

    # def normalize(self):
        # """Normalizes the wsj gainer data into the correct format."""
        # assert self.csv_path.endswith('.csv'),\
        # f'The file path {self.csv_path} does not end with a .csv'
        # output = pd.read_csv(self.csv_path, usecols =['Symbol', 'Price', 'Change', 'Change %'])


        # output = output.rename(columns={'Symbol':'symbol',
                                         # 'Price':'price', 
                                         # 'Change':'price_change', 
                                         # 'Change %':'price_percent_change'})

        # expected_cols = ['symbol', 'price', 'price_change', 'price_percent_change']

        # assert len(output.columns) == 4, f'Expected column length 4 but got {len(output.columns)}'

        # output['price'] = output['price'].str.split('+', n=1).str[0]

        # assert output.columns.values.tolist() == list(expected_cols),\
         # f'Expected column names of {expected_cols} but got {output.columns}'

        # output['price'] = output['price'].str.split('+', n=1).str[0]

        # print("Normalizing WSJ gainers")
        # return output

    # def save_with_timestamp(self):
        # """Saves the wsj dataset with the current timestamp."""
        # output = self.normalize()
        # timestamp = pd.to_datetime('now').strftime('%Y%m%d_%H%M%S')
        # out_path = f'wsjgainers_norm_{timestamp}.csv'
        # output.to_csv(out_path)
        # print("Saving WSJ gainers")


# TEMPLATE
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
    # Our sample main file would look like this
    # Make our selection, 'one' choice
    choice = sys.argv[1]

    # let our factory get select the family of objects for processing
    factory = GainerFactory(choice)
    downloader = factory.get_downloader()
    normalizer = factory.get_processor()

    # create our process
    runner = ProcessGainer(downloader, normalizer)
    runner.process()