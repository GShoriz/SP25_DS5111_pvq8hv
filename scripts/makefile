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
	sudo google-chrome-stable --headless --disable-gpu --dump-dom --no-sandbox --timeout=500 'https://www.wsj.com/market-data/stocks/us/movers' > wsjgainers.html

wsjgainers.csv: wsjgainers.html
	python -c "import pandas as pd; raw = pd.read_html('wsjgainers.html'); raw[0].to_csv('../sample_data/wsjgainers.csv')"

cnbcgainers.html:
	sudo google-chrome-stable --headless --disable-gpu --dump-dom --no-sandbox --timeout=5000 'https://www.cnbc.com/us-market-movers' > cnbcgainers.html


cnbcgainers.csv: cnbcgainers.html
	. env/bin/activate; python -c "import pandas as pd; raw = pd.read_html('cnbcgainers.html')[0]; raw.to_csv('../sample_data/cnbcgainers.csv')"


lint:
	@echo "Running pylint.."
	pylint ../bin/normalize_csv.py
	pylint ../bin/gainers/wsj.py
	pylint ../bin/gainers/yahoo.py
	pylint ../bin/gainers/cnbc.py
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
else ifeq ($(SRC), cnbc)
	@echo "Processing CNBC gainers..."
	. env/bin/activate; python ../bin/gainers/GainerProcessCNBC.py ../bin/gainers/cnbcgainers.csv
else
	@echo "Invalid source specified. Use SRC=yahoo, SRC=wsj, or SRC=cnbc."
endif

clean:
	rm -f ../scripts/yahoogainers.*
	rm -f ../scripts/wsjgainers.*
	rm -f ../scripts/cnbcgainers.*
	rm -f ../sample_data/yahoogainers.*
	rm -f ../sample_data/wsjgainers.*
	rm -f ../sample_data/wsjgainers.*
