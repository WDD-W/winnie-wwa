import requests
import json
import time
def rewards_txs(cls,last_block: int, address: str):
        page = 1
        rewards_list = []
        url = "https://hermes.to/api/lib/queries/getHermesDistributesByRecipient"

        payload = json.dumps({
        "params": {
            "recipient": address,
            "page": page,
            "limit": 100
        },
        "meta": {}
        })
        headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json'
        }
        while True:
            try:
                response = requests.request("POST", url, headers=headers, data=payload).json()
                rewards = response['result']
                if not rewards: 
                    return rewards_list
                for reward in rewards:
                    block = int(reward["block_height"])
                    if block > last_block:
                        rewards_list.append(reward)
                    else:
                        print(rewards_list)
                        return rewards_list
                page += 1
                print(page)
            except Exception as e:
                cls.logger.error("dot txs err", str(e))
        print(rewards)
        return rewards
def claimed_reward(cls, last_block: int, address: str):
        # cls.logger.info("iotx reward")
        result = []
        try:
            reward_list = rewards_txs("iotx",last_block, address)
            # print(reward_list)
            for reward in reward_list:
                block = int(reward["block_height"])
                hash = reward["action_hash"]
                tx_time = reward["timestamp"].split(".")[0]
                timeArray = time.strptime(tx_time,"%Y-%m-%dT%H:%M:%S")
                timestamp = time.mktime(timeArray)
                reward = {"currency": "iotx",
                            "reward_currency": "iotx",
                            "amount": float(reward["amount"]) / 1e18,
                            "address": address,
                            "hash":hash,
                            "block": block,
                            "block_time": int(timestamp)
                            }
                result.append(reward)
            print(result)
            return result
        except Exception as e:
            cls.logger.error("dot claimed_reward err", str(e))
        return None
        
# rewards_txs("a",17350522,"io1d6wpwx54a5ak00ffjy6lwryk05frrcjvpznpdz")
claimed_reward("a",17350522,"io1d6wpwx54a5ak00ffjy6lwryk05frrcjvpznpdz")