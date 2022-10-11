import requests
import json
import base64
content = '''<strong>AVAX投票到期监控</strong>
    <br>
    投票地址:
    <br>
    质押数量:5,530,000
    <br>
    到期时间:2022-7-31
    <br>
    剩余时间:11天
'''
url = "http://tool-robot.kumex.com:443/notify/encrypt_teams"
headers = {"XAK": "Rzsr5hTGpgrtbqcUMoFKhbDJZixEsPQ3AQ", "Content-Type": "application/json"}
source = {"cid": "19:68c7a4e9fccc4d23b00a3b7a5645685f@thread.v2", "content": content}
bstr = json.dumps(source).encode("utf-8")
data = base64.encodebytes(bstr).decode("utf-8")
ret = requests.post(url=url, headers=headers, data=data)
print(ret)