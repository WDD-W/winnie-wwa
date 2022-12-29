from decimal import Decimal


class RewardInfo:

    def __init__(self, reward_currency: str, reward_epoch: int, reward_time: int, address: str,
                 reward: Decimal,balance:Decimal,last_reward:Decimal,status:Decimal):
        self.reward_currency: str = reward_currency
        self.reward_epoch: int = reward_epoch
        self.reward_time: int = reward_time
        self.reward: Decimal = reward
        self.address: str = address
        self.balance: Decimal = balance
        self.last_reward:Decimal = last_reward
        self.status:Decimal = status

    def __repr__(self):
        return "RewardInfo(reward_currency='%s',reward_epoch='%d',reward_time=%d ,amount='%f'," \
               "address='%s' ,balance='%f', last_reward='%s',status='%s')" % (
                   self.reward_currency, self.reward_epoch, self.reward_time, self.reward,
                   self.address,self.balance,self.last_reward,self.status)
