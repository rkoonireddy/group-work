import numpy as np
from pandas_datareader import wb
from datetime import datetime
import pandas_datareader.data as web

def log_return(prices):
  return np.log(prices / prices.shift(1))

start = datetime(1999, 1, 1)
end = datetime(2019, 1, 1)

nasdaq_data = web.DataReader("NASDAQ100", "fred", start, end)
sap_data = web.DataReader("SP500", "fred", start, end)
gdp_data = wb.download(indicator='NY.GDP.MKTP.CD', country=['US'], start=start, end=end)
export_data = wb.download(indicator='NE.EXP.GNFS.CN', country=['US'], start=start, end=end)

nasdaq_returns = log_return(nasdaq_data['NASDAQ100'])

nasdaq_returns

sap_returns = log_return(sap_data['SP500'])

cov_mat = np.stack((nasdaq_data, gdp_data), axis = 0)

print('nasdaq_returns:', np.cov(cov_mat))