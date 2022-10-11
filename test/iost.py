import requests
def rewards_txs(last_block: int, address: str):
        rewards_list= []
        page = 1
        while True:
            url = "https://www.iostabc.com/api/account/%s/actions?type=bonus&page=%s&size=20" %  (address,page)
            headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json'
            }
            response = requests.request("GET", url, headers=headers).json()
            rewards = response['actions']
            # print(rewards)
            if not rewards:
                    print(rewards_list)
                    return rewards_list
            for reward in rewards:
                block = int(reward['block'])
                if block > last_block:
                    rewards_list.append(reward)
                else:
                    return rewards_list
            page += 1
        print(rewards_list)
        return rewards_list
rewards_txs(0,"kucoin_send")