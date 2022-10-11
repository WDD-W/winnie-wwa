import requests

url = "https://www.iostabc.com/endpoint/getTxByHash/CYj4wy9FCZJoHccv33VhwfrVo31uQgDV2NmZb3dCVrQ6"

payload = ""
headers = {
  'accept': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload).json()
mount = response["transaction"]["tx_receipt"]["receipts"][0]["content"].split("\"")[3]

print(mount)
