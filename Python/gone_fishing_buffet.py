# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 21:20:04 2019

@author: CHEO
"""

def gfb(ticker, df):
    
    legible_stock = True
    reason_list = []
    
    # EPS increases over the year (consistent)
    for growth in df.epsgrowth:
        if growth < 0:
            legible_stock = False
            reason_list.append('There is negative growth '+str(growth))
            break
    
    # ROE > 0.15
    if df.roe.mean() < 0.13:
        legible_stock = False
        reason_list.append('ROE mean is less than 0.13 '+str(df.roe.mean()))
    
    # ROA > 0.07 (also consider debt to equity cause Assets = Liabilities + Equity)
    if df.roa.mean() < 0.07:
        legible_stock = False
        reason_list.append('ROA mean is less than 0.07 '+str(df.roa.mean()))
        
    # Long term debt < 5 * Income
    if df.longterm_debt.tail(1).value[0] > 5*df.net_income.tail(1).values[0]:
        legible_stock = False
        reason_list.append('Long-term debt is 5 times the Net income')
        
    # Interest coverage ratio > 3
    if df.interest_coverage_ratio.tail(1).values[0] < 3:
        legible_stock = False
        reason_list.append('Interest coverage ratio is less than 3')
    
    # Print ticker, legible stock, reason list
    return reason_list