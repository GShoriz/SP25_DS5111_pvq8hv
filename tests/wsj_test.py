import os
import sys
import pandas as pd

sys.path.append('/home/ubuntu/SP25_DS5111_pvq8hv/bin/gainers')

from factory import GainerFactory

def test_wsj_download_and_process():
    """
    Test that WSJ downloading and processing is functioning correctly.
    """
    # Create factory and get WSJ specific downloader and processor
    factory = GainerFactory('wsj')
    downloader = factory.get_downloader()
    processor = factory.get_processor()

    # Download data
    downloader.download()
    assert os.path.exists('/home/ubuntu/SP25_DS5111_pvq8hv/scripts/wsjgainers.html'), "WSJ HTML not downloaded."

    # Normalize data
    processor.input_path = '/home/ubuntu/SP25_DS5111_pvq8hv/scripts/wsjgainers.html'
    processor.output_path = '/home/ubuntu/SP25_DS5111_pvq8hv/sample_data/wsjgainers.csv'
    processor.normalize()
    assert os.path.exists('/home/ubuntu/SP25_DS5111_pvq8hv/sample_data/wsjgainers.csv'), "WSJ CSV not created."

    # Check contents
    data = pd.read_csv('/home/ubuntu/SP25_DS5111_pvq8hv/sample_data/wsjgainers.csv')
    expected_columns = {'symbol', 'price', 'price_change', 'price_percent_change'}
    assert set(data.columns) == expected_columns, "CSV format incorrect."

    # Test save with timestamp function
    processor.save_with_timestamp(data)
    # Ensure a file is created with a timestamp
    timestamped_files = [f for f in os.listdir('/home/ubuntu/SP25_DS5111_pvq8hv/sample_data') if "wsjgainers_" in f]
    assert timestamped_files, "No timestamped file created."

if __name__ == "__main__":
    test_wsj_download_and_process()
