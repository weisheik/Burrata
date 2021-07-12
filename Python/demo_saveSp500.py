# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 22:29:04 2019

@author: CHEO
"""

import get_sp500_wiki as wiki

filepath = r'C:\Users\cheo\cheo\projects\burrata\burrata_python\hist'
filename = 'sp500_dict.csv'

stocks = wiki.getSp500()
wiki.exportCsv(stocks, filepath+'\\'+filename)
