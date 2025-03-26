import os
from datetime import datetime

folder_path = '/home/ubuntu/SP25_DS5111_aec4hr/datadump/'
# This block gets the current time on the OS and adds it to the file name
cur_time = str(datetime.fromtimestamp(datetime.now().timestamp()))[:-7]
fname = "ygainers_" + cur_time + '.csv'
fname = fname.replace(' ', '_')
# Rename the file name to new name
os.rename('ygainers.csv', folder_path+fname)

