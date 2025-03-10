"""
This module has a single function, import_csv which is created to 
import csv documents from scraped html websites that have been converted to csv.

Attributes:
    raw_csv_path: This represents the raw file path within your directory.

    """
import sys
import pandas as pd



def import_csv(raw_csv_path):
    """
	Imports a CSV and outputs it into a normalized format for processing.

	inputs:
		raw_csv_path: The raw file path to the csv for processing (STRING)

	returns:
		output: The normalized csv file converted into a pandas dataframe (DataFrame)
	"""

    assert raw_csv_path.endswith('.csv'),\
	 f'The file path {raw_csv_path} does not end with a .csv'

    output = pd.read_csv(raw_csv_path, usecols=['Symbol','Price', 'Change', 'Change %'])

    output = output.rename(columns=
	{'Symbol':'symbol', 'Price':'price', 'Change':'price_change', 'Change %':'price_percent_change'})

    expected_cols = ['symbol', 'price', 'price_change', 'price_percent_change']

    assert len(output.columns) == 4, f'Expected column length 4 but got {len(output.columns)}'

    assert output.columns.values.tolist() == list(expected_cols),\
     f'Expected column names of {expected_cols} but got {output.columns}'

    return output


def main():
    """
    The main function call for this module.
    """

    file_path = sys.argv[1]

    ygainers_norm = import_csv(file_path)


    out_path  = '~/SP25_DS5111_aec4hr/ygainers_norm.csv'
    ygainers_norm.to_csv(out_path)

if __name__ == "__main__":
    main()
