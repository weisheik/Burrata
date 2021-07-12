# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 20:54:48 2019

@author: CHEO
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

def getFinReport(ticker):
    # try:
    urlFinancial = 'https://marketwatch.com/investing/stock/'+ticker+'/financials'
    urlBalSheet = 'https://marketwatch.com/investing/stock/'+ticker+'/financials/balance-sheet'
    
    # Read in
    soupFinancial = BeautifulSoup(requests.get(urlFinancial).text, 'lxml')
    soupBalSheet = BeautifulSoup(requests.get(urlBalSheet).text, 'lxml')
    
    # Income statement
    titlesIncomeStatement = soupFinancial.findAll('td', {'class':'rowTitle'})
    epsList = []
    netIncomeList = []
    interestExpenseList = []
    ebitdaList = []
    
    for title in titlesIncomeStatement:
        if 'EPS (Basic)' in title.text:
            epsList.append([td.text for td in 
            title.findNextSiblings(attrs={'class':'valueCell'}) if td.text])
        if 'Net Income' in title.text:
            netIncomeList.append([td.text for td in
            title.findNextSiblings(attrs={'class':'valueCell'}) if td.text])
        if 'Interest Expense' in title.text:
            interestExpenseList.append([td.text for td in
            title.findNextSiblings(attrs={'class':'valueCell'}) if td.text])
        if 'EBITDA' in title.text:
            ebitdaList.append([td.text for td in
            title.findNextSiblings(attrs={'class':'valueCell'}) if td.text])
    
    # Balance sheet
    titlesBalSheet = soupBalSheet.findAll('td', {'class':'rowTitle'})
    equityList = []
    longtermDebtList = []
    
    for title in titlesBalSheet:
        if 'Total Shareholders\' Equity' in title.text:
            equityList.append([td.text for td in
            title.findNextSiblings(attrs={'class':'valueCell'}) if td.text])
        if 'Long-Term Debt' in title.text:
            longtermDebtList.append([td.text for td in
            title.findNextSiblings(attrs={'class':'valueCell'}) if td.text])
    
    # Variables
    eps = getElementList(epsList, 0)                            # eps = epsList[0]
    epsGrowth = getElementList(epsList, 1)                      # epsGrowth = epsList[1]
    netIncome = getElementList(netIncomeList, 0)                # netIncome = netIncomeList[0]
    equity = getElementList(equityList, 0)                      # equity = equityList[0]
    roa = getElementList(equityList, 1)                         # roa = equityList[1]
    longtermDebt = getElementList(longtermDebtList, 0)          # lontermDebt = longtermDebtList[0]
    interestExpense = getElementList(interestExpenseList, 0)    # interestExpense = interestExpenseList[0]
    ebitda = getElementList(ebitdaList, 0)                      # ebitda = ebitdaList[0]
    
    # Make it into dataframe
    df = pd.DataFrame({'eps':eps, 'epsgrowth':epsGrowth, 'netIncome':netIncome, 
                       'equity':equity, 'roa':roa, 'longtermDebt':longtermDebt, 
                       'interestExpense':interestExpense, 'ebitda':ebitda}, index=[2014,2015,2016,2017,2018])
    return df

#
def getElementList(list, element):
    try:
        return list[element]
    except:
        return '-'

#
def exportCsv(df, filename):
    df.to_csv(filename, index=False)
    
