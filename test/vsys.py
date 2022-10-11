import re
from turtle import st
import requests
import json

def latest_block(cls):
        url = "https://explorer.v.systems/api/blocks"
        headers = {'content-type': 'application/json'}
        payload = json.dumps({
            "pageNumber": 1,
            "pageSize": 0
        })
        try:
            response = requests.request("POST", url, headers=headers, data=payload).json()
            if response:
                print(int(response['data']['list'][0]['BlockId']))
                return int(response['data']['list'][0]['BlockId'])
        except Exception as e:
            print("block err", str(e))
        return 0

def available_balance(cls, address: str):
        url = "https://explorer.v.systems/api/addressDetail?address=%s" % address
        response = requests.get(url).json()['data']
        avai = float(response['available'][0:15])
        print(avai)
        return avai


def staked_balance(cls, address: str) -> list:
        url = "https://explorer.v.systems/api/addressDetail?address=%s" % address
        response = requests.get(url).json()['data']
        stake = float(response['LeaseOutBalance'])
        print(stake) 
        return stake


def trans_info1(address: str):
        rpc_server = "https://explorer.v.systems/api/addressTrans"
        headers = {'content-type': 'application/json'}

        payload = {
            "row": 50,
            "page": 0,
            "address": address,
            "pageNumber": 1, "pageSize": 20, "type": "2"
        }

        try:
            response = requests.post(
                rpc_server, data=json.dumps(payload), headers=headers).json()
        #     print(response['data']['List'])
            return response['data']['List']
        except Exception as e:
            print("VsysQuery account_info err ", str(e))
        return None



def claimed_reward(cls, last_block: int,address: str) -> list:
        all = 0
        reward_list = []
        payments = trans_info("vsys",last_block,address)
        # payments = trans_info1(address)
        print(payments)
        for payment in payments:
                block = payment['Height']
                amount_token: str = payment['Amount']
                amount = float(amount_token.split(" ")[0])
                fromAddr = payment['SenderAddress']
                # toAddr = payment['Recipient']
                timestamp = payment['TimeStamp'] / 1e6
                if block > last_block and fromAddr == "ARPhrZHzmUibVYRdhTtHT9r8nG1xciiytSF":
                        reward = {"currency": "vsys",
                                  "reward_currency": "vsys",
                                  "address": address,
                                  "block": block,
                                  "block_time": timestamp,
                                  "amount": amount}
                        reward_list.append(reward)
                else:
                        []
        print(reward_list)
        return reward_list


def trans_info(cls,last_block: int,address: str):
    page = 1
    result = []
    rpc_server = "https://explorer.v.systems/api/addressTrans"
    headers = {'content-type': 'application/json'}
    while True:
        try:
            payload = {
            "row": 50,
            "page": page,
            "address": address,
            "pageNumber": page, "pageSize": 100, "type": "2"
        }
            response = requests.post(
                rpc_server, data=json.dumps(payload), headers=headers).json()
            rewards = response['data']['List']
            if not rewards:
                return result
            for tx in rewards:
                    height =int(tx["Height"])
                    print(height,last_block)
                    if height > last_block:
                        result.append(tx)
                    else:
                        return result
            page += 1
            print(page)
            # print(result)
        except Exception as e:
            print("VsysQuery account_info err ", str(e))


claimed_reward("vsys",28875285,"ARPSZ4EGTygU39BtKctFa1cQzsUKYKtg7UU")
# latest_block("vsys")
# available_balance("vsys","ARPSZ4EGTygU39BtKctFa1cQzsUKYKtg7UU")
# staked_balance("vsys","ARPSZ4EGTygU39BtKctFa1cQzsUKYKtg7UU")
# trans_info("vsys",28875285,"ARPSZ4EGTygU39BtKctFa1cQzsUKYKtg7UU")
