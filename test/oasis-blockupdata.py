from ast import Num
from os import stat
import requests
import json
address = "oasis1qz68kwx74uqysx3mlnny4f32vj8ykrgdmgrt3g4x"

def blocks(address: str):
    url = "https://www.oasisscan.com/mainnet/validator/stats?address=oasis1qz68kwx74uqysx3mlnny4f32vj8ykrgdmgrt3g4x"

    payload = ""
    headers = {
    'accept': 'application/json',
    'authority': 'polkadot.webapi.subscan.io',
    'content-type': 'application/json',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36'
    }

    response = requests.request("GET", url, headers=headers, data=payload).json()
    status = response["data"]["signs"]
    # print(status)
    return status
# block(address)

def rates():
    T = 0
    F = 0
    num = 0
    stas = blocks(address)
    last_block = stas[-1]["height"]
    print("last_block:",last_block)
    # print("stas:",stas)
    for sta in stas:
        height = sta["height"]
        # print(height)
        # print(last_block)
        block = sta["block"]
        num += 1
        print(num)
        if height >= last_block and block is True:
            T += 1
        else:
            []
        print("height:",height,"status:",block)
    print("True:",T)
    print("num",num)
    rate = T / num * 100
    print(rate)
    return rate
print("block_status","  ",rates())
        




