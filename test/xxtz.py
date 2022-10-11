import requests
import json
from biz.core.core_modules import CoreModules
from db.orm.key_value import KeyValue
from db.dao.key_value_dao import KeyValueDao
from db.dao.sol_stake_account_dao import SolStakeAccountDao
from db.dao.transfer_dao import TransferDao
from sqlalchemy.engine.row import Row
from utils.logger import Logger
import logging
import time

# @CoreModules.register("xtz")
class Xtz(object):
    logger: logging.Logger = Logger().logger

    @classmethod
    def cgk_id(cls):
        return "xtz"

    @classmethod
    def reward(cls,address: str):
        rewards_list = []
        url = "https://api.tzkt.io/v1/rewards/delegators/%s?offset=0&limit=500" % (address)
        headers = {
        'accept': 'application/json',
        'apikey': 'airgap00391'
        }
        try:
            rewards = requests.request("get", url, headers=headers).json()
            # print(rewards)
            return rewards
        except Exception as e:
            print("XtzQuery reward error ", str(e))
            return None
   
    @classmethod
    def claimed_reward(cls, last_block: int,address:str) -> list:
        rewards = Xtz.reward(address)
        print(rewards)
        reward_infos = []
        if rewards:
            for item in rewards:
                amount = ( item['ownBlockRewards'] + item['ownBlockFees'] )/ 1e6            
                block = int(item["cycle"])
                reward_info = {"currency": "iost",
                    "reward_currency": "iost",
                    "amount": amount,
                    "address": address,
                    # "hash": hash,
                    "block": block,
                    # "block_time": timestamp
            }
                reward_infos.append(reward_info)
        print(reward_infos)
        return reward_infos
