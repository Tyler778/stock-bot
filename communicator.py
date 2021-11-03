import requests
import json
import os

api_key = os.environ['stock_key'];

def get_desc(ticker):
  url = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol=' + ticker + '&apikey=' + api_key
  r = requests.get(url)
  data = r.json()
  return data["Description"]

def get_pe(ticker):
  url = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol=' + ticker + '&apikey=' + api_key
  r = requests.get(url)
  data = r.json()
  return data["PERatio"]