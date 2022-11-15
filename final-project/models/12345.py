import pandas_datareader.data as web
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt


start_date = datetime(2018,3,1)
end_date = datetime(2022,3,1)

sap_data = web.DataReader(['FEDFUNDS', 'CBBTCUSD', 'CBETHUSD', 'CBLTCUSD'], 'fred', start_date, end_date)
sap_data

plt.show()
