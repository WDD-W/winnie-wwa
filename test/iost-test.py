import requests
import json
import time
def rewards_txs(cls, last_block: int, address: str):
            rewards_list= []
            page = 1
            while True:
                try:
                    url = "https://explorer.iost.io/api/txs?page=%s&account=%s&block=" % (page,address)
                    headers = {
                    'accept': 'application/json'
                    }

                    response = requests.request("GET", url, headers=headers).json()

                    rewards = response['data']['txsList']
                    if not rewards:
                            # print(rewards_list)
                            return rewards_list
                    for reward in rewards:
                        block = int(reward['blockHeight'])
                        if block > 69571415:
                            rewards_list.append(reward)
                        else:
                            return rewards_list
                    page += 1
                    print(page)
                print(rewards)
                    # return rewardss
                except Exception as e:
                    cls.logger.error("iost claimed_reward err", str(e))

def claimed_reward(cls,last_block:int,address:str):
    cls.logger.info("iost reward")
    result = []
    reward_list = rewards_txs("iost",last_block, address)
    try:
        for tx in reward_list:
            tx_time = tx['utcTime'].split(".")[0]
            timeArray = time.strptime(tx_time,"%Y-%m-%d %H:%M:%S")
            timestamp = time.mktime(timeArray)
            if tx["to"] == "vote_producer.iost":
                reward = {"currency": "iost",
                        "reward_currency": "iost",
                        "amount": float(tx['amount']),
                        "address": address,
                        "hash": tx['txHash'],
                        "block": int(tx['blockHeight']),
                        "block_time": timestamp
                }
                result.append(reward)
        print(result)
        return result
    except Exception as e:
        cls.logger.error("iost claimed_reward err", str(e))
    return None

rewards_txs("iost",69571415,"kucoin_iost")