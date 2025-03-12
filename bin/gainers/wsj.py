import pandas as pd
import sys


class GainerDownloadWSJ(GainerDownload):
    def __init__(self):
        from base import GainerDownload
        super().__init__('~/SP25_DS5111_aec4hr/ygainers.html')
        #pass

    def download(self):
        raw = pd.read_html(self.url)
        raw[0].to_csv('wsjgainers.csv')
        print("Downloading WSJ gainers")
        return raw
        
class GainerProcessWSJ(GainerProcess):
    def __init__(self, csv_path=None):
        from base import GainerProcess
        self.csv_path = csv_path if csv_path else 'wsjgainers.csv'
        #pass

    def normalize(self):
        assert self.csv_path.endswith('.csv'),f'The file path {self.csv_path} does not end with a .csv'
        output = pd.read_csv(self.csv_path, usecols =['Symbol', 'Price', 'Change', 'Change %'])
        

        output = output.rename(columns={'Symbol':'symbol', 'Price':'price', 'Change':'price_change', 'Change %':'price_percent_change'})
    
        expected_cols = ['symbol', 'price', 'price_change', 'price_percent_change']
    
        assert len(output.columns) == 4, f'Expected column length 4 but got {len(output.columns)}'
        
        output['price'] = output['price'].str.split('+', n=1).str[0]
        
        print("Normalizing WSJ gainers")
        return output

    def save_with_timestamp(self):
        output = self.normalize()
        timestamp = pd.to_datetime('now').strftime('%Y%m%d_%H%M%S')
        out_path = f'wsjgainers_norm_{timestamp}.csv'
        output.to_csv(out_path) 
        print("Saving WSJ gainers")