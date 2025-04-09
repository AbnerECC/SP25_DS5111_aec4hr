import sys
import os
sys.path.append('.')
import pandas as pd

from bin.normalize_csv import import_csv


def test_os_linux():
    assert os.name == 'posix' and 'linux' in os.uname().sysname.lower(), f"Operating system must be Linux, it is currently {os.name}"

def test_python_version():
    print(f'Python version: {sys.version}')
    assert sys.version_info[:2] in [(3,12), (3,13)], "Python version must be either 3.11 or 3.12"


def test_import_csv():

    test_csv = import_csv('./ygainers.csv')
    assert isinstance(test_csv, pd.DataFrame), f'Expected pandas df but got {type(test_csv)}'

  
