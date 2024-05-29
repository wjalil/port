import numpy as np
import pandas as pd
import requests
import xlsxwriter
import math
from secrets import iex_cloud_api
import csv
from sklearn.datasets import load_iris

def main():

    stocks=pd.read_csv('sp500_tracker.csv')
    my_columns=['Ticker','Stock Price','Market Cap','changePercent']
    final_dataframe=pd.DataFrame(data.data,columns=my_columns)
   
    for i in range(5):
        symbol=stocks.loc[i,"Ticker"]
        api_url=f'https://api.iex.cloud/v1/data/core/quote/{symbol}/quote/?token={iex_cloud_api()}'
        response=requests.get(api_url).json()
        try:
            final_dataframe=final_dataframe.append(pd.Series(
                [response[0]['symbol'],response[0]['latestPrice'],response[0]['marketCap'],response[0]['changePercent']*100],
                index=my_columns),ignore_index=True)
        except TypeError:
            print(i,"breal=k")

    data=load_iris()

    with pd.option_context('display.max_rows', None,
                       'display.max_columns', None,
                       'display.precision', 3,
                       ):

        print(final_dataframe.sort_values('changePercent'))
    
    
main()
