import requests
import json
import time
import datetime


def days(str1, str2):
    data1 = datetime.datetime.strptime(str1[0:10], "%Y-%m-%d")
    data2 = datetime.datetime.strptime(str2[0:10], "%Y-%m-%d")
    num = (data1 - data2).days
    return num


def ftm_gov():
    url = "https://xapi-nodeb.fantom.network/?"
    payload = json.dumps({
        "operationName": "DelegationsByAddress",
        "variables": {
            "address": "0x8710C7D1891076C66A11422dbf7dcECb601D3CBa",
            "count": 25,
            "cursor": None
        },
        "query": "query DelegationsByAddress($address: Address!, $cursor: Cursor, $count: Int!) {\n  delegationsByAddress(address: $address, cursor: $cursor, count: $count) {\n    pageInfo {\n      first\n      last\n      hasNext\n      hasPrevious\n      __typename\n    }\n    totalCount\n    edges {\n      cursor\n      delegation {\n        toStakerId\n        createdTime\n        amount\n        isDelegationLocked\n        lockedFromEpoch\n        lockedUntil\n        pendingRewards {\n          amount\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n"
    })
    headers = {
        'Content-Type': 'application/json'
    }
    res = requests.request("POST", url, headers=headers, data=payload)
    response = res.json()
    endtime = response["data"]["delegationsByAddress"]["edges"][0]["delegation"]["lockedUntil"]
    tran = time.localtime(int(endtime, 16))
    end = time.strftime("%Y-%m-%d %H:%M:%S", tran)
    now_time = time.localtime(time.time())
    now = time.strftime("%Y-%m-%d %H:%M:%S", now_time)
    day = days(end, now)

    print("end_time:", end)
    print("now_time:", now)
    print("days:", day)
ftm_gov()