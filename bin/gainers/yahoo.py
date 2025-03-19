"""Module for downloading and processing yahoo stock gainer data"""
#import sys
import pandas as pd


class GainerDownloadYahoo(GainerDownload):
    """Class to download the gainer data from yahoo."""
    def __init__(self):
        super().__init__('~/SP25_DS5111_aec4hr/ygainers.html') #Enter the default URL here
        #pass

    def download(self):
        """Downloads gainer data from the specified source."""
        raw = pd.read_html(self.url)
        raw[0].to_csv('ygainers.csv')
        print("Downloading yahoo gainers")
        return raw



class GainerProcessYahoo(GainerProcess):
    """Class for processing the gainer data from yahoo."""
    def __init__(self, csv_path=None):
        self.csv_path = csv_path if csv_path else 'ygainers.csv'
        #pass

    def normalize(self):
        """Normalizers the yahoo gainer data into the correct format."""
        assert self.csv_path.endswith('.csv'),\
        f'The file path {self.csv_path} does not end with a .csv'

        output = pd.read_csv(self.csv_path, usecols=['Symbol','Price', 'Change', 'Change %'])

        output = output.rename(
            columns={'Symbol':'symbol',
             'Price':'price',
              'Change':'price_change',
               'Change %':'price_percent_change'})

        expected_cols = ['symbol', 'price', 'price_change', 'price_percent_change']

        assert len(output.columns) == 4, f'Expected column length 4 but got {len(output.columns)}'

        assert output.columns.values.tolist() == list(expected_cols),\
         f'Expected column names of {expected_cols} but got {output.columns}'

        output['price'] = output['price'].str.split('+', n=1).str[0]

        print("Normalizing yahoo gainers")
        return output


    def save_with_timestamp(self):
        """Saves the yahoo dataset with the current timestamp."""
        output = self.normalize()
        timestamp = pd.to_datetime('now').strftime('%Y%m%d_%H%M%S')
        out_path = f'ygainers_norm_{timestamp}.csv'
        output.to_csv(out_path)
        ##out_path  = '~/SP25_DS5111_aec4hr/ygainers_norm.csv'
        print("Saving Yahoo gainers")