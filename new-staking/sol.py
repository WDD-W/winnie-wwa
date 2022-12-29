import requests
import time 
from datetime import datetime, timedelta
import xlwt
import json

def export_excel(currency):
    workbook = xlwt.Workbook(encoding="utf-8")

    sheet1 = workbook.add_sheet(currency)

    sheet1.write(0, 0, "币种")
    sheet1.write(0, 1, "链")
    sheet1.write(0, 2, "hash")
    sheet1.write(0, 3, "块高")
    sheet1.write(0, 4, "交易类型")
    sheet1.write(0, 5, "时间")
    sheet1.write(0, 6, "余额变动")
    sheet1.write(0, 7, "手续费")
    sheet1.write(0, 8, "交易前余额")
    sheet1.write(0, 9, "交易后余额")
    row = 1
    items = claimed_reward("sol",130679769,"Eyv5miAz6Y3qPMHZjGZEm1U5Ud28HX9d15MHMzMRApv5")

    for item in items:
        sheet1.write(row, 0, item["currency"])
        sheet1.write(row, 1, item["chain"])
        sheet1.write(row, 2, item["hash"])
        sheet1.write(row, 3, item["block"])
        sheet1.write(row, 4, item["txtype"])
        sheet1.write(row, 5, item["block_time"])
        sheet1.write(row, 6, item["amount"])
        sheet1.write(row, 7, item["fee"])
        sheet1.write(row, 8, item["pre"])
        sheet1.write(row, 9, item["post"])
        row += 1

    workbook.save("staking-profit-%s.xls" % currency)

def txs(cls, last_block: int, address: str):
        new_txs = []
        txhash = ""
        try:
            while True:
                url = "https://api.solscan.io/account/transaction?address=%s&before=%s" % (address, txhash)
                print("sol txs url", url)
                headers = {'user-agent': 'python3.8'}
                response = requests.get(url, headers=headers).json()
                items = response['data']
                if not items or len(items) == 0:
                    return new_txs
                for item in items:
                    slot = item['slot']
                    if slot > last_block:
                        new_txs.append(item)
                        txhash = item["txHash"]
                    else:
                        return new_txs
        except Exception as e:
            print("sol txs err", str(e))

def transfers(cls, address: str):
        limit = 100
        offset = 0
        url = "https://api.solscan.io/account/soltransfer/txs?address=%s&limit=%s&offset=%s" % (address, limit, offset)
        headers = {'user-agent': 'python3.8'}
        response = requests.get(url, headers=headers).json()
        return response["data"]["tx"]["transactions"]

        return new_txs
def stake_addresses(cls, address):
        try:
            url = "https://public-api.solanabeach.io/v1/account/%s/stakes?limit=100&offset=0" % address
            headers = {
                "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}
            response = requests.get(url, headers=headers).json()
            result = []
            for account in response["data"]:
                result.append(account["pubkey"]["address"])
            print(result)
            return result
        except Exception as e:
            cls.logger.error("sol stake_addresses err %s" % str(e))
        return None

def account_balance(tx: str):
    url = "https://public-api.solscan.io/transaction/%s" % tx

    payload = ""
    headers = {
    'accept': 'application/json',
    'user-agent': 'python3.8'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    ac = response.json()["inputAccount"]

    for res in ac:
        # print(res)
        if res["account"] == "Eyv5miAz6Y3qPMHZjGZEm1U5Ud28HX9d15MHMzMRApv5":
            preBalance = res["preBalance"]
            postBalance = res["postBalance"]
    print(preBalance,postBalance)
    return [preBalance,postBalance]




def claimed_reward(cls, last_block: int, address: str):
        headers = {
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}
        try:
            addresses = stake_addresses("sol",address)
            result = []

            for stake_address in addresses:
                cursor = ""
                loop = True
                while loop:
                    url = "https://public-api.solanabeach.io/v1/account/%s/stake-rewards?cursor=%s" % (stake_address, cursor)
                    print('cursor', cursor)
                    rep = requests.get(url, headers=headers).json()
                    if len(rep) == 0:
                        loop = False
                        continue
                    for reward_ in rep:
                        # print(reward_)
                        # print(reward_["postBalance"])
                        if reward_['effectiveSlot'] > last_block:
                            block_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(reward_['timestamp'])))
                            epoch = stake_address + str(-reward_["epoch"])
                            reward = {"currency": "sol",
                                      "reward_currency": "sol",
                                      "chain" : "Sol",
                                      "hash":epoch,
                                      "txtype":"REWARD",
                                      "address": stake_address,
                                      "fee":0,
                                      "amount": reward_['amount'] / 1e9,
                                      "block": reward_['effectiveSlot'],
                                      "block_time": block_time,
                                      "address": address,
                                      "pre":"",
                                      "post": float((reward_["postBalance"]) / 1e9)
                                      }
                            result.append(reward)
                        else:
                            loop = False
                            break
                        cursor = str(reward_["epoch"])
            trxs = transfers("sol", address)
            for trx in trxs:
                height = int(trx["slot"])
                block_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(trx["blockTime"])))
                hash = trx["txHash"]
                fromAddr = trx["src"]
                amount = float(trx["lamport"] / 1e9)
                fee = float(trx["fee"] / 1e9)
                account = account_balance(hash)
                if height > last_block:
                    if fromAddr == "Eyv5miAz6Y3qPMHZjGZEm1U5Ud28HX9d15MHMzMRApv5":
                        amount = -amount
                    reward = {"currency": "sol",
                            "reward_currency": "sol",
                            "chain":"Sol",
                            "amount": amount,
                            "address": address,
                            "txtype":"TRANSFER",
                            "fee":fee,
                            "hash":hash,
                            "block": height,
                            "block_time": block_time,
                            "pre":float(int(account[0]) /1e9),
                            "post":float(int(account[1]) /1e9)
                            }
                    result.append(reward)
            ts = txs("sol", last_block,address)
            for trx in ts:
                height = int(trx["slot"])
                block_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(trx["blockTime"])))
                hash = trx["txHash"]
                # fromAddr = trx["src"]
                type = trx["parsedInstruction"][-1]["type"]
                amount = float(trx["lamport"] / 1e9)
                fee = float(trx["fee"] / 1e9)
                account = account_balance(hash)
                if type != "sol-transfer" :
                    reward = {"currency": "sol",
                            "reward_currency": "sol",
                            "chain":"Sol",
                            "amount": amount,
                            "address": address,
                            "txtype":type,
                            "hash":hash,
                            "fee" :fee,
                            "block": height,
                            "block_time": block_time,
                            "pre":float(int(account[0]) /1e9),
                            "post":float(int(account[1]) /1e9)
                            }
                    result.append(reward)
            print(result)
            return result
        except Exception as e:
            cls.logger.error("sol claimed_reward err %s" % str(e))
        return None
# claimed_reward("sol",130679770,"Eyv5miAz6Y3qPMHZjGZEm1U5Ud28HX9d15MHMzMRApv5")
# stake_addresses("sol","Eyv5miAz6Y3qPMHZjGZEm1U5Ud28HX9d15MHMzMRApv5")
export_excel("sol")
# account_balance("2XnEssDUMUsBjj8T5mgce3fkevi65i54KapRt3orx158Medzg4y5ZN1jfEFdTCAKxTbMhGKpPMDefFfJyQfQu5o4")