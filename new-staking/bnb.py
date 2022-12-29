import requests
import time 
from datetime import datetime, timedelta
import xlwt
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
    items = claimed_reward("bnb",248543477,"bnb18e925lnsd7df99ehdcpphc9we8rdtuw2gn3zv6")

    for item in items:
        sheet1.write(row, 0, item["currency"])
        sheet1.write(row, 1, item["chain"])
        sheet1.write(row, 2, item["hash"])
        sheet1.write(row, 3, item["block"])
        sheet1.write(row, 4, item["txtype"])
        sheet1.write(row, 5, item["block_time"])
        sheet1.write(row, 6, item["amount"])
        sheet1.write(row, 7, item["txfee"])
        sheet1.write(row, 8, item["block_time"])
        sheet1.write(row, 9, item["block_time"])
        row += 1

    workbook.save("staking-profit-%s.xls" % currency)

def txs(cls, last_block: int, address: str):
        page = 1
        headers = {'content-type': 'application/json'}
        txs_list = []
        while True:
            try:
                url = "https://explorer.bnbchain.org/api/v1/txs?page=%s&rows=25&address=%s" % (page, address)
                response = requests.get(url, headers=headers).json()
                txArray = response['txArray']
                # if not txArray:
                #     return txs_list
                # for tx in txArray:
                #     if int(tx["blockHeight"]) > 247316156:
                #         txs_list.append(tx)
                #     else:
                #         print(txs_list)
                #         return txs_list
                # page += 1
                print(txArray)
                return txArray
            except Exception as e:
                cls.logger.error("bnb txs err", str(e))
                return txs_list
        return txs_list

def claim_txs(cls, last_block: int, address: str):
        offset = 0
        headers = {'content-type': 'application/json'}
        rewards_list = []
        while True:
            try:
                url = "https://api.binance.org/v1/staking/chains/bsc/delegators/%s/rewards?limit=100&offset=%s" % (
                    address, offset)
                response = requests.get(url, headers=headers).json()
                rewards = response['rewardDetails']
                if not rewards:
                    return rewards_list
                for reward in rewards:
                    if int(reward["height"]) > last_block:
                        rewards_list.append(reward)
                    else:
                        return rewards_list
                offset += 100
            except Exception as e:
                cls.logger.error("bnb claim txs err", str(e))
        return rewards_list

def claimed_reward(cls, last_block: int, address: str):
        # cls.logger.info("bnb reward")
        result = []
        try:
            reward_list = claim_txs("bnb",last_block, address)
            trxs = txs("bnb",last_block, address)
            for reward in reward_list:
                height = int(reward["height"])
                reward_time = datetime.strptime(reward["rewardTime"].split(".")[0], "%Y-%m-%dT%H:%M:%S") + timedelta(
                    hours=8)
                block_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(datetime.timestamp(reward_time)))
                hash = reward["id"]
                if height > last_block:
                    reward = {"currency": "bnb",
                              "reward_currency": "bnb",
                              "chain":"BNB",
                              "amount": float(reward["reward"]),
                              "address": address,
                              "hash":hash,
                              "txfee":0,
                              "txtype":"REWARD",
                              "block": height,
                              "block_time": block_time
                              }
                    result.append(reward)
            for trx in trxs:
                height = int(trx["blockHeight"])
                block_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(trx["timeStamp"]/1000)))
                hash = trx["txHash"]
                txtype = trx["txType"]
                fromAddr = trx["fromAddr"]
                amount = float(trx["value"])
                txfee = trx["txFee"]
                if txtype == "TRANSFER" and fromAddr == "bnb18e925lnsd7df99ehdcpphc9we8rdtuw2gn3zv6":
                    amount = -amount
                reward = {"currency": "bnb",
                        "reward_currency": "bnb",
                        "chain":"BNB",
                        "amount": amount,
                        "address": address,
                        "hash":hash,
                        "block": height,
                        "txfee":txfee,
                        "hash":hash,
                        "txtype":txtype,
                        "block_time": block_time
                        }
                result.append(reward)
            print(result)
            return result
        except Exception as e:
            cls.logger.error("bnb claimed_reward err", str(e))
        return None
export_excel("bnb")