# from msilib import add_stream
import requests
# from db.dao.transfer_dao import TransferDao
# from biz.core.core_modules import CoreModules
# from utils.logger import Logger
import logging
import time
import json
# from utils.tx_utils import TxType

addr = "persistence1lctnzd6gky9eq0rkzvtr6anuy7p8tpysckczv9"
atom = "cosmos1uer4mwcq2vlt8l23ncwyjj70mug5pzx82cvlyw"
def available_balance(cls, address: str):
    # print("xprt available_balance")
    url = "https://lcd-persistence.cosmostation.io/cosmos/bank/v1beta1/balances/%s" % address
    try:
        rep = requests.get(url).json()
        # print(rep['balances'])
        print(float(rep['balances'][-1]['amount']) / 1e6)
        return float(rep['balances'][-1]['amount']) / 1e6
    except Exception as e:
        return 0

def staked_balance(address: str) -> float:
    url = "https://lcd-persistence.cosmostation.io/cosmos/staking/v1beta1/delegations/%s" % address
    try:
        rep = requests.get(url).json()
        print(float(rep['delegation_responses'][0]['balance']['amount']) / 1e6)
        return float(rep['delegation_responses'][0]['balance']['amount']) / 1e6
    except Exception as e:
        return 0

def unstaking_balance(address: str) -> float:
        url = "https://lcd-persistence.cosmostation.io/cosmos/staking/v1beta1/delegators/%s/unbonding_delegations" % address
        headers = {'content-type': 'application/json'}
        try:
            response = requests.get(url, headers=headers).json()
            undelegations = response["unbonding_responses"]
            unstaking_amount = 0
            for undelegation in undelegations:
                entries = undelegation["entries"]
                for entry in entries:
                    unstaking_amount += entry["balance"]
            print(float(unstaking_amount) / 1e6)
            return float(unstaking_amount) / 1e6
        except Exception as e:
            print("xprt unstaking_balance err", str(e))
        return None  

def unclaimed_reward(cls, address: str):
        print("reward")
        url = "https://lcd-persistence.cosmostation.io/cosmos/distribution/v1beta1/delegators/%s/rewards" % address
        headers = {'content-type': 'application/json'}
        try:
            reward_list = []
            response = requests.get(url, headers=headers).json()
            rewards = response['total']
            for denom in rewards:
                reward = {"currency": "xprt",
                          "reward_currency": "xprt",
                          "amount": float(denom["amount"]) / 1e6}
                reward_list.append(reward)
            print(reward_list)
            return reward_list
        except Exception as e:
            print("xprt unclaimed_reward err", str(e))
        return None
# @classmethod
# def txs(address: str):
#     url = "https://api-persistence.cosmostation.io/v1/account/new_txs/%s?from=0&limit=50" % address
#     try:
#         rep = requests.get(url).json()
#         return rep
#     except Exception as e:
#         return None

# # @classmethod
# def latest_block():
#     url = "https://api-persistence.cosmostation.io/v1/status"
#     try:
#         rep = requests.get(url).json()
#         if "block_height" in rep.keys():
#             print(int(rep["block_height"]))
#             return int(rep["block_height"])
#         return None
#     except Exception as e:
#         return None

# # @classmethod
# def validator_info(validator_address):
#     url = "https://api-persistence.cosmostation.io/v1/staking/validator/%s" % validator_address
#     try:
#         rep = requests.get(url).json()
#         if "tokens" in rep.keys():
#             return float(rep["tokens"]) / 1e6
#         return None
#     except Exception:
#         return None



# # @classmethod
# def claim_info(last_block: int,address:str):
#     reward_list = []
#     txList = txs(address)
#     reward = 0
#     block_time = 0
#     if not isinstance(txList, list):
#         return []
#     for tx in txList:
#         messages = tx["data"]["tx"]["body"]["messages"]
#         # height = int(tx["data"]["height"])
#         # ts = time.strptime(tx["data"]["timestamp"], "%Y-%m-%dT%H:%M:%SZ")
#         # block_time = time.mktime(ts)
#         for msg in messages:
#                 if msg["@type"] == "/cosmos.distribution.v1beta1.MsgWithdrawDelegatorReward" \
#                         or msg["@type"] == "/cosmos.staking.v1beta1.MsgUndelegate" \
#                         or msg["@type"] == "/cosmos.staking.v1beta1.MsgBeginRedelegate" \
#                         or msg["@type"] == "/cosmos.distribution.v1beta1.MsgWithdrawValidatorCommission":
#                     has_reward = True
#                     type = msg["@type"]
#                     ts = time.strptime(tx["data"]["timestamp"], "%Y-%m-%dT%H:%M:%SZ")
#                     block_time = time.mktime(ts)
#                     height = int(tx["data"]["height"])
#                     continue
#         if height <= last_block:
#             continue
#         msg = json.loads(tx["data"]['raw_log'])
#         for obj in msg:
#             events = obj["events"]
#             for event in events:
#                 if event["type"] == "withdraw_rewards" or event["type"] == "withdraw_commission":
#                     value = "".join(list(filter(str.isdigit, event["attributes"][0]["value"])))
#                     reward += float(value) / 1e6
#                     rewards = {"currency": "xprt",
#                                     "reward_currency": "xprt",
#                                     "amount": float(value) / 1e6,
#                                     "address": address,
#                                     "block": height,
#                                     "block_time": block_time}
#                     reward_list.append(rewards)
#         logs = tx["data"]["logs"]
#         for log in logs:
#             if type == "/cosmos.distribution.v1beta1.MsgWithdrawDelegatorReward":
#                 for event in log["events"]:
#                     if event["type"] == "withdraw_rewards":
#                         attributes = event["attributes"]
#                         for attribute in attributes:
#                             value = attribute["value"]
#                             print("value", value)
#                             if attribute["key"] == "amount":
#                                 reward = {"currency": "atom",
#                                             "reward_currency": "atom",
#                                             "address": address,
#                                             "block": block,
#                                             "block_time": block_time,
#                                             "amount": float(value[:-5]) / 1e6}
#                                 reward_list.append(reward)
#                                 break
#             elif type == "/cosmos.staking.v1beta1.MsgUndelegate":
#                 unbond_amount = ""
#                 for event in logs["events"]:
#                     if event["type"] != "unbond":
#                         attributes = event["attributes"]
#                         for attribute in attributes:
#                             if attribute["key"] == "amount":
#                                 unbond_amount = attribute["value"]
#                 for event in logs["event"]:
#                     if event["type"] != "transfer":
#                         attributes = event["attributes"]
#                         for attribute in attributes:
#                             if attribute["key"] == "amount" and attribute["value"] != unbond_amount:
#                                 reward = {"currency": "atom",
#                                             "reward_currency": "atom",
#                                             "amount": float(attribute["value"][:-5]) / 1e6,
#                                             "address": address,
#                                             "block": block,
#                                             "block_time": block_time}
#                                 reward_list.append(reward)
#                                 break
#             elif type == "/cosmos.staking.v1beta1.MsgBeginRedelegate" or type == "/cosmos.staking.v1beta1.MsgDelegate":
#                 for event in log["events"]:
#                     if event["type"] == "transfer":
#                         attributes = event["attributes"]
#                         for attribute in attributes:
#                             if attribute["key"] == "amount":
#                                 reward = {"currency": "atom",
#                                             "reward_currency": "atom",
#                                             "amount": float(attribute["value"][:-5]) / 1e6,
#                                             "address": address,
#                                             "block": block,
#                                             "block_time": block_time}
#                                 reward_list.append(reward)
#                                 break
#         if type == "/cosmos.distribution.v1beta1.MsgWithdrawValidatorCommission":
#             for tag in tx["data"]["tags"]:
#                 if tag["key"] == "commission":
#                     reward = {"currency": "atom",
#                                 "reward_currency": "atom",
#                                 "amount": float(tag["value"][:-5]) / 1e6,
#                                 "address": address,
#                                 "block": block,
#                                 "block_time": block_time}
#                     reward_list.append(reward)
#                     break
#     return reward_list
#     print(reward_list)
#     return reward_list
# claim_info(0,"persistence1lctnzd6gky9eq0rkzvtr6anuy7p8tpysckczv9")


def claimed_reward(cls, last_block: int, address: str):
        print("claimed_reward")
        try:
            reward_list = []
            txs1 = txs(cls,last_block, address)
            for tx in txs1:
                if "code" not in tx["data"].keys():
                    continue
                has_reward = False
                messages = tx["data"]["tx"]["body"]["messages"]
                type = None
                block_time = 0
                block = 0
                if not messages:
                    continue
                for msg in messages:
                    if msg["@type"] == "/cosmos.distribution.v1beta1.MsgWithdrawDelegatorReward" \
                            or msg["@type"] == "/cosmos.staking.v1beta1.MsgUndelegate" \
                            or msg["@type"] == "/cosmos.staking.v1beta1.MsgBeginRedelegate" \
                            or msg["@type"] == "/cosmos.distribution.v1beta1.MsgWithdrawValidatorCommission":
                        has_reward = True
                        type = msg["@type"]
                        ts = time.strptime(tx["data"]["timestamp"], "%Y-%m-%dT%H:%M:%SZ")
                        block_time = time.mktime(ts)
                        block = int(tx["data"]["height"])
                        continue
                if not has_reward or not type:
                    continue
                logs = tx["data"]["logs"]
                for log in logs:
                    if type == "/cosmos.distribution.v1beta1.MsgWithdrawDelegatorReward":
                        for event in log["events"]:
                            if event["type"] == "withdraw_rewards":
                                attributes = event["attributes"]
                                for attribute in attributes:
                                    value = attribute["value"]
                                    print("value", value)
                                    if attribute["key"] == "amount":
                                        reward = {"currency": "xprt",
                                                  "reward_currency": "xprt",
                                                  "address": address,
                                                  "block": block,
                                                  "block_time": block_time,
                                                  "amount": float(value[:-5]) / 1e6}
                                        reward_list.append(reward)
                                        break
                    elif type == "/cosmos.staking.v1beta1.MsgUndelegate":
                        unbond_amount = ""
                        for event in logs["events"]:
                            if event["type"] != "unbond":
                                attributes = event["attributes"]
                                for attribute in attributes:
                                    if attribute["key"] == "amount":
                                        unbond_amount = attribute["value"]
                        for event in logs["event"]:
                            if event["type"] != "transfer":
                                attributes = event["attributes"]
                                for attribute in attributes:
                                    if attribute["key"] == "amount" and attribute["value"] != unbond_amount:
                                        reward = {"currency": "xprt",
                                                  "reward_currency": "xprt",
                                                  "amount": float(attribute["value"][:-5]) / 1e6,
                                                  "address": address,
                                                  "block": block,
                                                  "block_time": block_time}
                                        reward_list.append(reward)
                                        break
                    elif type == "/cosmos.staking.v1beta1.MsgBeginRedelegate" or type == "/cosmos.staking.v1beta1.MsgDelegate":
                        for event in log["events"]:
                            if event["type"] == "transfer":
                                attributes = event["attributes"]
                                for attribute in attributes:
                                    if attribute["key"] == "amount":
                                        reward = {"currency": "xprt",
                                                  "reward_currency": "xprt",
                                                  "amount": float(attribute["value"][:-5]) / 1e6,
                                                  "address": address,
                                                  "block": block,
                                                  "block_time": block_time}
                                        reward_list.append(reward)
                                        break
                if type == "/cosmos.distribution.v1beta1.MsgWithdrawValidatorCommission":
                    for tag in tx["data"]["tags"]:
                        if tag["key"] == "commission":
                            reward = {"currency": "xprt",
                                      "reward_currency": "xprt",
                                      "amount": float(tag["value"][:-5]) / 1e6,
                                      "address": address,
                                      "block": block,
                                      "block_time": block_time}
                            reward_list.append(reward)
                            break
            print(reward_list)
            return reward_list
        except Exception as e:
            print("xprt claimed_reward err", str(e))
        return None

    # limit max 50
    # from: tx id
    # @classmethod
def txs(cls, last_block: int, address: str):
    result = []
    offset = 0
    while True:
        url = "https://api-persistence.cosmostation.io/v1/account/new_txs/%s?from=%s&limit=50" % (address, offset)
        try:
            response = requests.get(url).json()
            if not isinstance(response, list) or not response:
                return result
            for tx in response:
                # print("tx 000 ", tx)
                if int(tx["data"]["height"]) <= last_block:
                    return result
                else:
                    result.append(tx)
                    offset = int(tx["header"]["id"])
        except Exception as e:
            cls.logger.error("xprt txs err %s" % str(e))
    return result
claimed_reward("xprt", 0, "persistence1lctnzd6gky9eq0rkzvtr6anuy7p8tpysckczv9")