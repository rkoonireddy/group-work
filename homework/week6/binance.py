import requests
import datetime
import pandas as pd
import time
from tabulate import tabulate


ROOT_URL = "https://api.binance.com"
ENDPOINT = "/api/v3/klines"


Exact_date = '01/09/2022'

specific_time = 1000 * int(time.mktime(datetime.datetime.strptime(Exact_date, '%d/%m/%Y').timetuple()))

# Request string URL
request_for_observations = "{root_url}{endpoint}?symbol={currencypair}&interval={interval}&startTime={startTime}&limit={limit}" \
        .format(root_url=ROOT_URL,
                endpoint=ENDPOINT,
                currencypair="BTCUSDT",
                interval="1m",
                startTime=specific_time,
                limit=75
        )
print(request_for_observations)

# send request to Binance and get response
req_res = requests.get(request_for_observations)
print(req_res)

data = pd.DataFrame.from_records(
        req_res.json(),
        columns=["Open time", "Open", "High", "Low", "Close", "Volume", "Close time", 
        "Quote asset vol.", "Number of trades", "Taker buy base asset vol.", "Taker buy quote asset vol.", "Ignore" 
        ]
    )
data.index = data.pop("Open time").map(lambda x: datetime.datetime.fromtimestamp(x/1000))
print(data) 

with open('table123.txt', 'w') as f:  # to print the data into a .txt file
    f.write(tabulate(data))