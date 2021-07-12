# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 21:59:27 2019

@author: CHEO
"""

import quandl

#
def DataFeedQuandl(ticker):
    QUANDL_API_KEY = 'DDr5TqyAo-Y7fyuumuEt'
    quandl.ApiConfig.api_key = QUANDL_API_KEY
    price = quandl.get('WIKI/'+ticker)
    return price
    