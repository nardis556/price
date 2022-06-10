import ccxt
import time
import config

exchange = ccxt.binance()

while True:
    try:
        ticker = exchange.fetch_ticker(symbol=config.ticker1)['bid']
        print(ticker)
        time.sleep(5)
    except Exception as e:
        print(e)
