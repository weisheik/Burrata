# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 01:02:51 2019

@author: CHEO
"""

import get_finReport_marketwatch as marketwatch

filepath = r'C:\Users\cheo\cheo\projects\burrata\burrata_python\hist'
filename = 'intc_fmw.csv'

finReport = marketwatch.getFinReport('intc')
marketwatch.exportCsv(finReport, filepath+'\\'+filename)