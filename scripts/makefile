default:
	@cat makefile

env:
	python3 -m venv env; . env/bin/activate; pip install --upgrade pip

update: env
	. env/bin/activate; pip install -r requirements.txt

yahoogainers.html:
	sudo google-chrome-stable --headless --disable-gpu --dump-dom --no-sandbox --timeout=5000 'https://finance.yahoo.com/markets/stocks/gainers/?start=0&count=200' > yahoogainers.html

yahoogainers.csv: yahoogainers.html
	python -c "import pandas as pd; raw = pd.read_html('yahoogainers.html'); raw[0].to_csv('../sample_data/yahoogainers.csv')"

wsjgainers.html:
	sudo google-chrome-stable --headless --disable-gpu --dump-dom --no-sandbox --timeout=5000 'https://www.wsj.com/market-data/stocks/us/movers' > wsjgainers.html

wsjgainers.csv: wsjgainers.html
	python -c "import pandas as pd; raw = pd.read_html('wsjgainers.html'); raw[0].to_csv('../sample_data/wsjgainers.csv')"

sanalysisgainers.html:
	sudo google-chrome-stable --headless --disable-gpu --dump-dom --no-sandbox --timeout=5000 'https://stockanalysis.com/markets/gainers/' > sanalysisgainers.html
sanalysisgainers.csv: sanalysisgainers.html
	python -c "import pandas as pd; raw = pd.read_html('sanalysisgainers.html'); raw[0].to_csv('../sample_data/sanalysisgainers.csv')"


lint:
	@echo "Running pylint.."
	pylint ../bin/normalize_csv.py
	pylint ../bin/gainers/wsj.py
	pylint ../bin/gainers/yahoo.py
	pylint ../bin/gainers/sanalysis.py
	pylint ../bin/gainers/base.py
	pylint ../bin/gainers/factory.py
	pylint ../bin/get_gainer.py

test: lint
	@echo "Running pytest.."
	pytest -vvx ../tests

gainers:
ifeq ($(SRC), yahoo)
	@echo "Processing Yahoo gainers..."
	. env/bin/activate; python ../bin/gainers/GainerProcessYahoo.py ../bin/gainers/ygainers.csv
else ifeq ($(SRC), wsj)
	@echo "Processing WSJ gainers..."
	. env/bin/activate; python ../bin/gainers/GainerProcessWSJ.py ../bin/gainers/wsjgainers.csv
else ifeq ($(SRC), sanalysis)
	@echo "Processing STOCKANALYSIS gainers..."
	. env/bin/activate; python ../bin/gainers/GainerProcessSANALYSIS.py ../bin/gainers/sanalysisgainers.csv
else
	@echo "Invalid source specified. Use SRC=yahoo, SRC=wsj, or SRC=sanalysis."
endif

clean:
	rm -f ../scripts/yahoogainers.html
	rm -f ../scripts/wsjgainers.html
	rm -f ../scripts/sanalysisgainers.html
	rm -f ../sample_data/yahoogainers.csv
	rm -f ../sample_data/wsjgainers.csv
	rm -f ../sample_data/sanalysisgainers.csv

clean_yahoo:
	rm -f ../scripts/yahoogainers.html
	rm -f ../sample_data/yahoogainers.csv
clean_wsj:
	rm -f ../scripts/wsjgainers.html
	rm -f ../sample_data/wsjgainers.csv

clean_sanalysis:
	rm -f ../scripts/sanalysisgainers.html
	rm -f ../sample_data/sanalysisgainers.csv
