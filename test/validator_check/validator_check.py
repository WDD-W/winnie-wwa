import requests
import json
from load_json import pub_k

#备用url
# def check():
#     pub_keys = pub_k()
#     try:
#         for pub_key in pub_keys:
#             url = "https://beaconcha.in/api/v1/validator/%s" % pub_key
#             # print(url)
#             response = requests.request("GET", url).json()
#             status = response["status"].split(":")[0]
#             # print(status)
#             if status == "ERROR":
#                 node = "未注册"
#             elif status == "OK":
#                 node = "已存在"
#             else:
#                 node = "error"
#             print(pub_key,node)
            
#     except Exception as e:
#         print("url requests error")


def check():
    pub_keys = pub_k()
    try:
        for pub_key in pub_keys:
            url = "https://beacon-rpc.ebunker.io/eth/v1/beacon/states/head/validators/0x%s" % pub_key
            # print(url)
            response = requests.request("GET", url).json().get("code")
            # print(response)
            if response == 404:
                node = "未注册"
            elif response == None:
                node = "已存在"
            else:
                node = "error"
            print(pub_key,node)
            
    except Exception as e:
        print("url requests error")

check()

