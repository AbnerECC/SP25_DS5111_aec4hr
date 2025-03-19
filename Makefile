default:
	@cat Makefile

env:
	python3 -m venv env; . env/bin/activate; pip install --upgrade pip

update: env
	. env/bin/activate && pip install -r requirements.txt

ygainers.html:
	sudo google-chrome-stable --headless --disable-gpu --dump-dom --no-sandbox --timeout=5000 'https://finance.yahoo.com/markets/stocks/gainers/?start=0&count=200' > ygainers.html

ygainers.csv: ygainers.html
	python3 -c "import pandas as pd; raw = pd.read_html('ygainers.html'); raw[0].to_csv('ygainers.csv')"

wsjgainers.html:
	sudo google-chrome-stable --headless --disable-gpu --dump-dom --no-sandbox --timeout=30000 'https://www.wsj.com/market-data/stocks/us/movers' > wsjgainers.html

wsjgainers.csv: wsjgainers.html
	python3 -c "import pandas as pd; raw = pd.read_html('/home/ubuntu/SP25_DS5111_aec4hr/wsjgainers.html'); raw[0].to_csv('wsjgainers.csv')"

lint:
	. env/bin/activate && pylint /home/ubuntu/SP25_DS5111_aec4hr/bin || true

test: lint
	. env/bin/activate;  pytest -vv tests

gainers:
	@if [ -z "$(SRC)" ]; then \
    echo "Error: Must input SRC Parameter"; \
    echo "Usage: make gainers SRC=yahoo"; \
    echo "   or: make gainers SRC=wsj"; \
    exit 1; \
  fi
	@echo "Processing gainers from $(SRC)..."
	@python3 get_gainer.py $(SRC)

clean:
	rm ygainers.* || true
	rm wsjgainers.* || true
	rm wsjgainers_norm* || true
	rm ygainers_norm* || true