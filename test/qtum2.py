import requests
# def claimed_reward(cls,last_block: int, address: str):
#         # cls.logger.info("dot reward")
#         result = []
#         try:
#             reward_list = rewards_txs("dot",last_block, address)
#             for reward in reward_list:
#                 height = int(reward["event_index"].split("-")[0])
#                 index = reward["extrinsic_index"]
#                 trx_time = get_local_format_time(int(reward["block_timestamp"]))
#                 if height > last_block:
#                     reward = {"currency": "dot",
#                               "address": address,
#                               "reward_currency": "dot",
#                               "amount": float(reward["amount"]) / 1e10,
#                               "hash":index,
#                               "block": height,
#                               "block_time": trx_time
#                               }
#                     result.append(reward)
#             print(result)
#             return result
#         except Exception as e:
#             cls.logger.error("dot claimed_reward err", str(e))
#         return None

def rewards_txs(cls,last_block: int, address: str):
    rewards_list = []
    limit = 100
    page = 1
    offset = page * limit
    last_block += 1
    url = "https://qtum.info/api/address/%s/basic-txs?limit=%d&offset=%d&fromBlock=%d&toBlock=999999999" % (
        address, limit, offset, last_block)
    while True:
        try:
            response = requests.get(url).json()
            rewards = response['transactions']
            if not rewards:
                return rewards_list
            for reward in rewards:
                block = reward['blockHeight']
                if block > last_block:
                    rewards_list.append(reward)
                else:
                    print(rewards_list)
                    return rewards_list
            page += 1
        except Exception as e:
            cls.logger.error("qtum txs err", str(e))
    return rewards_list
rewards_txs("qtum",0,"QdkhRUY73y5crTi2obDLyf4fqoxrFfJCnE")