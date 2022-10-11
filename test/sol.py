import requests
def claimed_reward(cls, last_block: int, address: str):
        headers = {
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}
        stake_address = "5zF4rvLJLhNNps9ZX67E8zQgzz1zmQ8QoKpSUcLdNVXm"
        reward_list = []
        url = "https://public-api.solanabeach.io/v1/account/5zF4rvLJLhNNps9ZX67E8zQgzz1zmQ8QoKpSUcLdNVXm/stake-rewards?cursor=330"
        # print('cursor', cursor)
        rep = requests.get(url, headers=headers).json()
        print(rep)
        return rep
claimed_reward("vsys",0,"Eyv5miAz6Y3qPMHZjGZEm1U5Ud28HX9d15MHMzMRApv5")