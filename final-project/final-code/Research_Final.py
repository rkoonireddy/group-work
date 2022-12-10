import pandas_datareader.data as web
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
plt.style.use('fivethirtyeight')


#Define period
start = dt.datetime(2018,1,1)        
end = dt.datetime(2022, 11, 11) 


#Define the cryptocurrencies and Treasury yield
symbols = ['BTC-USD', 'ETH-USD', 'XRP-USD', 
           'LTC-USD', '^CMC200', '^TNX']

#Bitcoin, Etherium, Ripple, Litecoin, CMC Crypto 200 Index by Solacti, 10 yr treasury yield respectfuly

#Define source API as yahoo
source = 'yahoo'

#Retrieve the data, specificaly the closing prices
data = web.DataReader(symbols, source, start, end)['Adj Close']

#Show data
data.head()


# SAVING A DATAFRAME WITH PARQUET 
data.to_parquet('data_small.parquet',compression='BROTLI')


data_normal = pd.read_parquet('data_small.parquet')

data_normal

#Rename the symbols so we can call them more easily. The ^ makes it hard to reference the Treasury yield
data.rename(columns = {'^CMC200':'CMC200', '^TNX':'TNX', 'BTC-USD':'BTC', 'ETH-USD':'ETH', 'XRP-USD':'XRP', 'LTC-USD':'LTC'}, inplace = True)
data.loc[:, data.columns!='TNX'].plot.line(figsize=(20,6), grid = True, title='Cryptocurrencies price movement 2018-2022') #Excluding TNX


plt.legend()


#Plot XRP price movement
data['XRP'].plot.line(figsize=(20,6), grid = True, title='Ripple price movement 2018-2022') #Ripple
plt.legend()


#Plot CMC200 price movement
data['CMC200'].plot.line(figsize=(20,6), grid = True, title='Crypto 200 Index price movement 2018-202') 
plt.legend()


#Plot TNX price movement
data['TNX'].plot.line(figsize=(20,6), grid = True, title='10 yr Treasury Yield 2018-2022') #Treasury Yield 10 Years
plt.legend()


#Plot BTC & ETH price movement
data['BTC'].plot.line(figsize=(20,6), grid = True, title='BTC vs ETH price movement 2018-2022')
data['ETH'].plot.line(figsize=(20,6), grid = True, title='BTC vs ETH price movement 2018-2022')
plt.legend()


#Replacing Null values into zeros
data.fillna(0) 

#When changing the data into percantages there will be NaN values so we have to clean that up also
data_pct = data.pct_change(periods=1).dropna()

#show the transformed data
data_pct.head()


# SAVING A DATAFRAME WITH PARQUET 
data_pct.to_parquet('data_adjusted_small.parquet',compression='BROTLI')


data_adj = pd.read_parquet('data_adjusted_small.parquet')


data_adj


#mean of each financial instrument
data_adj.mean()

data_adj.mean().plot.bar()


#Standard deviation for each of the cryptocurrencies
data_adj.loc[:, data.columns!='TNX'].std().plot.bar()


#Mean Absolute Deviation 
data_adj.loc[:, data.columns!='TNX'].mad()


#Skewness
data_adj.loc[:, data.columns!='TNX'].skew().plot.barh()


#Plot BTC & TNX price movement
data_adj['BTC'].plot()
data_adj['TNX'].plot()
plt.legend()
plt.title('Bitcoin and Treasury yield % change 2019-2022')


#Covariance of our transformed data
cov = data_adj.cov()


#Plot Covariance between indicators
cov.plot()
plt.legend()
plt.title('Covariance between indicators')



#Show the covariance heatmap
cov.iloc[:,-1:]


fig, ax = plt.subplots(figsize=(10, 8))

sns.heatmap(cov,vmin=-0.0002,
            cmap=sns.color_palette("Reds",100),
            square=True, ax=ax, annot=True)



#Correlation and corresponding heatmap for our dataset
#Here the method of calculating the correlation is with Pearson's coefficient
#Pearson’s coefficient measures linear correlation

corr = data_adj.corr(method='pearson')

print(corr)

#The correlation between the 10yr treasury yield and other cryptocurrencies is very weak and shows negligible correlation.
#The interesting fact is if we compare BTC to other cryptos we see very high positive correlation.

fig, ax = plt.subplots(figsize=(8, 6))

sns.heatmap(corr,vmin=0,vmax=1,
            cmap=sns.color_palette("Reds",100),
            square=True, ax=ax, annot=True)



#Plot Correlation between indicators
corr.plot()
plt.legend()
plt.title('Correlation between indicators')



#Measuring correlation with the sperman method
#The Spearman's rank coefficient of correlation
#is a nonparametric measure of rank correlation (statistical dependence of ranking between two variables

data_adj.corr(method='spearman')


#As seen from the results the correlation between the 10yr treasury yield and other cryptocurrencies is very weak
#For them to be at least moderatily correlated, the Spearman correlation coefficient would have to be greater than 0.40 in absolute terms.
#We conclude that there is no significant correlation between interest rate hikes and cryptocurrency exchange rates




