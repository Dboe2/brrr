import yfinance as fin
from datetime import datetime
import csv

file = csv.reader(open('stocklist.csv'), delimiter=',')
for line in file:
   try:
      ticker = str(line[0]) # which stock to search for
      ticker_handle = fin.Ticker(ticker) # ticker handler
      company_name = ticker_handle.info.get('shortName')

      shareSHT = ticker_handle.info.get('sharesShort')
      shareFLT = ticker_handle.info.get('floatShares')
      if shareFLT is not None:
         pSHT = shareSHT/shareFLT * 100
         if pSHT > 100:
            print(line[0])
            print(pSHT)
   except Exception as e:
      pass
