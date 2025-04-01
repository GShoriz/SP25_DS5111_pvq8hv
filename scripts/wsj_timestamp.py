import os
from datetime import datetime
storage_path = '/home/ubuntu/SP25_DS5111_pvq8hv/sample_data/'
current_time = datetime.now().strftime("%Y-%m-%d_%H-%M") 
filename = "wsjoogainers" + current_time + ".csv"
filename = filename.replace(' ','_')
os.rename('wsjgainers.csv', storage_path + filename)
