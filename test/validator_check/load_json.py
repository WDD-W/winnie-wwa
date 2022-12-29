import json
import os
filePath = './deposit/'
list_data=os.listdir(filePath)
def pub_k():
    pub=[]
    for src in list_data:
        road = "./deposit/" + src
        with open(road,'r')  as load_f :
            load_dict = json.load(load_f)
            for i in load_dict:
                pub_key = str(i["pubkey"])
                pub.append(pub_key)
                print(pub_key,src)
    return pub
