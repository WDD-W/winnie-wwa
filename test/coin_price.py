import requests
import json
import xlwt

response = requests.get("https://www.kucoin.com/_api/currency/prices?base=USD&targets=&lang=zh_CN")
data = response.json()
price = data["data"]


print(price)