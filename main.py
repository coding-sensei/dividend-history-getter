import requests
import json

url = "https://seekingalpha.com/market_data/xignite_token"

payload = {}
headers = {
      'Accept': '*/*',
        'X-Requested-With': 'XMLHttpRequest',
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
          }

token = requests.request("GET", url, headers=headers, data = payload).json()

print(token)

ticker = "aapl"
data_api_url = f"https://globalhistorical.xignite.com/v3/xGlobalHistorical.json/GetCashDividendHistory?IdentifierType=Symbol&Identifier={ticker}&StartDate=01/01/1800&EndDate=12/30/2022&IdentifierAsOfDate=&CorporateActionsAdjusted=true&_token={token['_token']}&_token_userid={token['_token_userid']}"

print(data_api_url)

dividend_history = requests.request("GET", data_api_url).json()

print(dividend_history)

with open('history.json', 'w') as f:
      json.dump(dividend_history, f)
