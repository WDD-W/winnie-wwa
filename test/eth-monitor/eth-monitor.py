from asyncio import transports
import requests
import time
import json
from reward_info import RewardInfo
from db.db_dao import Session
from db.reward import Reward
from sqlalchemy.sql import exists

#获取验证者状态
def rewards() :
    reward_list = []
    now_time = time.localtime(time.time())
    now = time.strftime("%Y-%m-%d %H:%M:%S", now_time)
    pub_keys = ["0x8a094a10bb067925adc6e43833db3fef88f4a9920eeec5b44e410fbc54faa295d50dbb68c395b7102a5779179f2960ef","0xb9c3b984d2c26767d85a3345cad0401479aec1004a6c71a83c1239e429555a8b27ee15e20bd76d9cbf470cab5508547a"]
    try:
        for pub_key in pub_keys:
            url = "https://beaconcha.in/api/v1/validator/%s" % pub_key
            response = requests.request("GET", url).json()
            balance = response["data"]["balance"] / 1e9
            reward_ = balance  - 32
            slot = response["data"]["lastattestationslot"]
            last = last_reward(Session(),pub_key)
            status = response["data"]["status"]
            # print(balance,reward_,last)
            reward_info = RewardInfo(reward_currency="ETH",
                                reward_epoch=slot,
                                reward_time=time.time(),
                                address=pub_key,
                                reward=reward_,
                                balance=balance,
                                last_reward=last,
                                status=status
            )
            reward_list.append(reward_info)
    except Exception as e:
        print("reward error url")
    print(now,reward_list)
    return reward_list


#数据库写操作
def query():
    reward_info = rewards()
    start_time = time.time()
    try:
        session = Session()
        for info in reward_info:
            new_reward = Reward(
                currency="ETH", 
                pub_key=info.address, 
                reward=info.reward, 
                block = info.reward_epoch, 
                timestamp=info.reward_time
            )
            session.add(new_reward)
            print("found new reward timestamp=%d  block=%d currency=%s reward=%f address=%s" % (
                            info.reward_time, info.reward_epoch, "ETH",
                            info.reward, info.address))
            session.commit()
    except Exception as e:
        print("reward query error %s" % str(e), query)
    end_time = time.time()
    print("reward query thread use %d s" % (end_time - start_time))

#访问数据库，读取上一条收益数量、时间、slot
def last_reward(session: Session,pub_key:str):
    try:
        exi = session.query(exists().where(Reward.pub_key== pub_key)).scalar()
        if exi is True:
            last_reward_info: Reward = session.query(Reward).filter(Reward.pub_key == pub_key).order_by(
                Reward.block.desc()).offset(1).first() 
            print(last_reward_info)
            if last_reward_info is None: 
                last_reward_info: Reward = session.query(Reward).filter(Reward.pub_key == pub_key).order_by(
                Reward.block.desc()).offset(0).first()
                last_reward = last_reward_info.reward
                last_slot = last_reward_info.block
                last_time = last_reward_info.timestamp
            else:
                last_reward = last_reward_info.reward
                last_slot = last_reward_info.block
                last_time = last_reward_info.timestamp
        else:
            last_reward = 0
            last_slot = 0
            last_time = 0
        # print(last_reward,last_epoch)
    except Exception as e:
        print("load sql error")
    return last_reward,last_time,last_slot

#计算导出数据
def info():
    all_reward = rewards()
    content = []
    content.append("## ETH验证者监控")
    i = 1
    for info in all_reward:
        pub_key=info.address, 
        reward_=info.reward,  
        balance = info.balance
        status = info.status
#计算收益slot间隔
        slot = info.reward_epoch,
        last_slot = info.last_reward[2]
        reward_slot = int(slot[0]) - last_slot
        print(last_slot,slot)
#计算收益时间段
        last_time = info.last_reward[1]
        now_time = time.time()
        reward_time = now_time-last_time
        print(reward_time)
#计算收益差及apy
        last = info.last_reward[0]
        per_reward = float(reward_[0]) - last
        # print(last,reward_,per_reward)
        num = per_reward / reward_time * 3600 * 24 * 365 / 32
        apy = ('%.2f%%' % (num*100))
        # print(last,reward_,per_reward,num,apy)
        content.append("### 验证者%d" % i)
        content.append("#### 公钥: https://beaconcha.in/validator/%s" % pub_key)
        content.append("#### 验证者状态: %s" % status)
        content.append("#### 余额: %s" % balance)
        content.append("#### 收益: %.6f / %s slot" %(per_reward,reward_slot))
        content.append("#### APY: %s" % apy)
        content.append("#### 链上APY: 4.2%")
        i+=1
        content.append("----------------------")
        if num < 0.003 :
            content.append('注意!!收益率低于3%')
            # content.append('注意!!收益率低于3%' + ''.join(list(map(lambda x: "@" + x, ['+86-13791315513']))))
        else:
            content.append('收益正常')
    print(content)
#发送数据
    all_data = {
            "msgtype": "markdown",
            "markdown": {
                "title": "ETH收益监控",
                "text": "\n".join(content)
            },
        }

    # send_ding(all_data)

#发送dingding
def send_ding(data):
        url = 'https://oapi.dingtalk.com/robot/send?access_token=c25555bd92dbed483422184c5c05e1bcb643105d452024008a85399135efd029'
        json_data = json.dumps(data).encode(encoding="utf-8")

        header_encoding = {'User-Agent': 'Python3.9',
                           "Content-Type": "application/json"}
        res = requests.post(url, data=json_data, headers=header_encoding).json()
        print(res)


query()
info()
# last_reward(Session(),"0xb77c9dbx135cd8f8b7fa6cc6bca36944a6d26cbe993549f08e90f70d3804f46c1313b2585568aebd9f9ce3ce6e18e248")