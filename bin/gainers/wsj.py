"""Module for processing gainer data for WSJ."""
#import sys
import pandas as pd
from base import GainerDownload, GainerProcess


class GainerDownloadWSJ(GainerDownload):
    """Class to download the gainer data from WSJ."""
    def __init__(self):
        super().__init__('~/SP25_DS5111_aec4hr/wsjgainers.html')
        #pass

    def download(self):
        """Downloads gainer data from the specified source."""
        raw = pd.read_html(self.url)
        raw[0].to_csv('wsjgainers.csv')
        print("Downloading WSJ gainers")
        return raw

class GainerProcessWSJ(GainerProcess):
    """Class for processing the gainer data from WSJ."""
    def __init__(self, csv_path=None):
        self.csv_path = csv_path if csv_path else 'wsjgainers.csv'
        #pass

    def normalize(self):
        """Normalizes the wsj gainer data into the correct format."""
        assert self.csv_path.endswith('.csv'),\
        f'The file path {self.csv_path} does not end with a .csv'
        output = pd.read_csv(self.csv_path, usecols =['Unnamed: 0', 'Last', 'Chg', '% Chg'])


        output = output.rename(columns={'Unnamed: 0':'symbol',
                                         'Last':'price', 
                                         'Chg':'price_change', 
                                         '% Chg':'price_percent_change'})

        expected_cols = ['symbol', 'price', 'price_change', 'price_percent_change']

        assert len(output.columns) == 4, f'Expected column length 4 but got {len(output.columns)}'

        output['symbol'] = output['symbol'].str.extract(r'\((.*?)\)')

        assert output.columns.values.tolist() == list(expected_cols),\
         f'Expected column names of {expected_cols} but got {output.columns}'

        print("Normalizing WSJ gainers")
        return output

    def save_with_timestamp(self):
        """Saves the wsj dataset with the current timestamp."""
        output = self.normalize()
        timestamp = pd.to_datetime('now').strftime('%Y%m%d_%H%M%S')
        out_path = f'wsjgainers_norm_{timestamp}.csv'
        output.to_csv(out_path)
        print("Saving WSJ gainers")