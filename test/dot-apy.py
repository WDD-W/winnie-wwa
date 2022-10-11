import requests
import json
import time
import datetime
address = "1kyH6C7sivf9Q6r1ahZqKDywH1jkSY7uvCkhB1zwLVYgtsg"

def days(str1,str2):
  data1=datetime.datetime.strptime(str1[0:10],"%Y/%m/%d")
  data2=datetime.datetime.strptime(str2[0:10],"%Y/%m/%d")
  num1 = (data1-data2).days
  return num1

def bonded(address: str):
        url = "https://polkadot.webapi.subscan.io/api/v2/scan/search"
        payload = json.dumps({
        "key": address,
        "row": 1,
        "page": 0
        })
        headers = {
        'accept': 'application/json',
        'authority': 'polkadot.webapi.subscan.io',
        'content-type': 'application/json',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36'
        }
        response = requests.request("POST", url, headers=headers, data=payload).json()
        bond = float(response["data"]["account"]["bonded"]) / 1e10
        print("bond",bond)
        return bond

def rewards():
    url = "https://polkadot.webapi.subscan.io/api/v2/scan/account/reward_slash"
    payload = json.dumps({
    "row": 100,
    "page": 0,
    "is_stash": True,
    "address": address
    })
    headers = {
    'accept': 'application/json',
    'authority': 'polkadot.webapi.subscan.io',
    'content-type': 'application/json',
    'user-agent': 'Python3.8'
    }
    response = requests.request("POST", url, headers=headers, data=payload).json()


    list = response["data"]["list"]
    
    num = 0
    all = 0
    for reward in list:
        if num < 70:
            mount = float(reward["amount"]) / 1e10
            times = int(reward["block_timestamp"])
            print(mount)
            num +=1
            all +=mount
    print("times",times)
    time_local = time.localtime(times)
    end = time.strftime("%Y/%m/%d %H:%M:%S",time_local)
    now_time = time.localtime(time.time())
    now = time.strftime("%Y/%m/%d %H:%M:%S",now_time)
    day = days(now,end) + 2
    print("day:",day)

    print("num",num,"all:",all)
    apy = all / day * 365 / bonded(address)
    print("APY:",apy)
rewards()