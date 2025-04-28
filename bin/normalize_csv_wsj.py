"""
This module has a single function, import_csv which is created to 
import csv documents from scraped html websites that have been converted to csv.

Attributes:
    raw_csv_path: This represents the raw file path within your directory.

    """
import sys
import os
import pandas as pd
from datetime import datetime



def import_csv(raw_csv_path):
    """Normalizes the wsj gainer data into the correct format."""
    assert raw_csv_path.endswith('.csv'),\
    f'The file path {raw_csv_path} does not end with a .csv'
    
    filename = os.path.basename(raw_csv_path)
    
    filename = filename.replace(':','_')
    
    # Grab the file date time information
    datetime_str = filename.split('_', 1)[1].replace('.csv', '')
    date_part, hour, minute, second = datetime_str.split('_')
    formatted_datetime_str = f"{date_part} {hour}:{minute}:{second}"
    dt = datetime.strptime(formatted_datetime_str, "%Y-%m-%d %H:%M:%S")
    
    output = pd.read_csv(raw_csv_path, usecols =['Unnamed: 0', 'Last', 'Chg', '% Chg'])


    output = output.rename(columns={'Unnamed: 0':'symbol',
                                        'Last':'price', 
                                        'Chg':'price_change', 
                                        '% Chg':'price_percent_change'})

    expected_cols = ['symbol', 'price', 'price_change', 'price_percent_change']

    assert len(output.columns) == 4, f'Expected column length 4 but got {len(output.columns)}'

    output['symbol'] = output['symbol'].str.extract(r'\((.*?)\)')
    assert output.columns.values.tolist() == list(expected_cols),\
        f'Expected column names of {expected_cols} but got {output.columns}'
    
    output['timestamp'] = dt



    print("Normalizing WSJ gainers")
    return output


def main():
    """
    The main function call for this module.
    """

    file_path = sys.argv[1]

    wsjgainers_norm = import_csv(file_path)
    
    filename = os.path.basename(file_path)
    
    output_dir = '~/SP25_DS5111_aec4hr/bin/normalized_gainers'
    
    os.makedirs(output_dir, exist_ok=True)


    out_path  = os.path.join(output_dir, filename)
    wsjgainers_norm.to_csv(out_path)

if __name__ == "__main__":
    main()
