# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 22:11:12 2019

@author: CHEO
"""

import DataFeedQuandl

price = DataFeedQuandl.DataFeedQuandl('AAPL')

#%%

import matplotlib.pyplot as plt

price.plot();

#%%

filepath = r'C:\Users\cheo\cheo\projects\burrata\burrata_python\hist'
filename = 'appl_price.csv'

price.to_csv(filepath+'\\'+filename, index=False)