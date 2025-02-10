import numpy as np
import pandas as pd
import sys




file_path = sys.argv[1]


def import_csv(raw_csv_path):
    
    assert raw_csv_path.endswith('.csv'), f'The file path provided does not end with a .csv'
    
    output = pd.read_csv(raw_csv_path, usecols=['Symbol','Price', 'Change', 'Change %'])
    output = output.rename(columns={'Symbol':'symbol', 'Price':'price', 'Change':'price_change', 'Change %':'price_percent_change'})
    
    expected_cols = ['symbol', 'price', 'price_change', 'price_percent_change']
    
    assert len(output.columns) == 4, f'Expected column length 4 but got {len(output.columns)}'
    assert output.columns.values.tolist() == list(expected_cols), f'Expected column names of {expected_cols} but got {output.columns}'
    
    
    return output

ygainers_norm = import_csv(file_path)


out_path = '~/SP25_DS5111_aec4hr/ygainers_norm.csv'
ygainers_norm.to_csv(out_path)
