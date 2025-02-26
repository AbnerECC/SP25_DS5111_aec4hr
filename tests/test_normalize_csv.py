import sys
sys.path.append('.')
import pandas as pd

from bin.normalize_csv import import_csv



def test_import_csv():

    test_csv = import_csv('./ygainers.csv')
    assert isinstance(test_csv, pd.DataFrame), f'Expected pandas df but got {type(test_csv)}'
