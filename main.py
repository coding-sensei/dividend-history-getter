import requests
import json
from datetime import *
import csv
import operator

def get_stock_history(ticker):
    url = "https://seekingalpha.com/market_data/xignite_token"

    payload = {}
    headers = {
          'Accept': '*/*',
            'X-Requested-With': 'XMLHttpRequest',
              'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
              }

    token = requests.request("GET", url, headers=headers, data = payload).json()

    data_api_url = f"https://globalhistorical.xignite.com/v3/xGlobalHistorical.json/GetCashDividendHistory?IdentifierType=Symbol&Identifier={ticker}&StartDate=01/01/1800&EndDate=12/30/2022&IdentifierAsOfDate=&CorporateActionsAdjusted=true&_token={token['_token']}&_token_userid={token['_token_userid']}"
    print(data_api_url)

    dividend_history = requests.request("GET", data_api_url).json()

    return dividend_history

def get_stocks_from_file(path):
    with open(path, "r") as file:
        return [stock.strip() for stock in file]

def get_latest_ticker_dividends(dividend_history):
    sorted_dividends = dividend_history['CashDividends']
    sorted_dividends.sort(key = operator.itemgetter('PayDate'), reverse=True)

    dividends = [ dividend for dividend in sorted_dividends if date.fromisoformat(dividend['PayDate']) >= date.today()]

    return [ dict(dividend, ticker=dividend_history['Identifier']) for dividend in dividends]

paying_companies = []
for ticker in get_stocks_from_file("stocks.txt"):
    ticker_history = get_stock_history(ticker)
    paying_companies.extend(get_latest_ticker_dividends(ticker_history))

with open('stock_pay_dates.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Ticker','Declared Date','Ex-Dividend Date','Payout Date', 'Amount'])
    paying_companies.sort(key = operator.itemgetter('PayDate'))
    for dividend in paying_companies:
        row = [ dividend['ticker'],
                dividend['DeclaredDate'],
                dividend['ExDate'],
                dividend['PayDate'],
                dividend['DividendAmount']]
        writer.writerow(row)
