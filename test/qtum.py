import requests
def tx(address: str, last_block: int):
        reward = 0
        max_block = 0
        max_timestamp = 0
        rewards_list = []
        # 多找一个块的数据，保证全
        found_last_block = False
        limit = 100
        page = 1
        offset = page * limit
        last_block += 1
        url = "https://qtum.info/api/address/%s/basic-txs?limit=%d&offset=%d&fromBlock=%d&toBlock=999999999" % (
            address, limit, offset, last_block)
        try:
            response = requests.get(url).json()
            txs = response['transactions']
            if len(txs) == 0:
                found_last_block = True
            else:
                for tx in txs:
                    block = tx['blockHeight']
                    timestamp = tx['timestamp']
                    tx_type = tx['type']
                    hash = tx['id']
                    if tx_type == 'block-reward':
                        amount = float(tx['amount']) / 1e8
                        if block > max_block:
                            max_block = block
                            max_timestamp = timestamp
                        reward = {"currency": "qtum",
                              "reward_currency": "qtum",
                              "amount": amount,
                              "address": address,
                              "hash":hash,
                              "block": block,
                              "block_time": timestamp
                              }
                        rewards_list.append(reward)
                    if block <= last_block:
                        found_last_block = True

        except Exception as e:
            e.with_traceback()
            print('qtum balance err', str(e))
        print(rewards_list)
        return rewards_list
tx("QdkhRUY73y5crTi2obDLyf4fqoxrFfJCnE",0)