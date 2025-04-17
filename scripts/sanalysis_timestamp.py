import os
from datetime import datetime
storage_path = '/home/ubuntu/SP25_DS5111_pvq8hv/sample_data/'
current_time = datetime.now().strftime("%Y-%m-%d_%H-%M") 
filename = "sanalysisgainers" + current_time + ".csv"
filename = filename.replace(' ','_')
source_file_path = os.path.join(storage_path, 'sanalysisgainers.csv')
destination_file_path = os.path.join(storage_path, filename)
os.rename(source_file_path, destination_file_path)
