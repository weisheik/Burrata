# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 21:43:06 2019

@author: CHEO
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

# Get S&P500 stocks names
def getSp500():
    print("Getting SP500 stocks names from Wikipedia")
    
    resp = requests.get('http://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soup = BeautifulSoup(resp.text, 'lxml')
    table = soup.find('table', {'class': 'wikitable sortable'})
    
    stocks = []
    symbols = []
    securities = []
    sectors = []
    industries = []
    
    for row in table.findAll('tr')[1:]:
        symbol = row.findAll('td')[0].text
        security = row.findAll('td')[1].text
        sector = row.findAll('td')[3].text
        industry = row.findAll('td')[4].text
        
        symbols.append(symbol.lower().rstrip())
        securities.append(security)
        sectors.append(sector.lower())
        industries.append(industry.lower())
        
    stocks.append(symbols)
    stocks.append(securities)
    stocks.append(sectors)
    stocks.append(industries)
    
    stocksDf = pd.DataFrame(stocks).T
    stocksDf.columns = ['symbol','security','sector','industry']
    stocksDf['index'] = 'SP500'
    
    return stocksDf

# Export dataframe to CSV
def exportCsv(df, filename):
    df.to_csv(filename, index=False)
    