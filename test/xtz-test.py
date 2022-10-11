import  requests
import json
def reward(cls,address: str):
        offset = 0
        rewards_list = []
        import requests
        url = "https://tezos-mainnet-conseil.prod.gke.papers.tech/v2/data/tezos/mainnet/operations"

        payload = json.dumps({
        "predicates": [
            {
            "field": "destination",
            "set": [
                "tz1iUvwxAWPkR8aop4Xxa9WtTrm766PnxxdN"
            ],
            "operation": "eq",
            "group": "A0"
            }
        ]
        })
        headers = {
        'accept': 'application/json',
        'apikey': 'airgap00391',
        'Content-Type': 'application/json'
        }
        try:
            rewards = requests.request("POST", url, headers=headers,data=payload).json()
            print(rewards)
            return rewards
        except Exception as e:
            print("XtzQuery reward error ", str(e))

        return None
reward("xtz","tz1iUvwxAWPkR8aop4Xxa9WtTrm766PnxxdN")