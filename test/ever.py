import requests
import json
import subprocess

def block_behind():
        url = "https://api.everscan.io/v1/stats"
        headers = {
        'accept': 'application/json'
        }

        response = requests.request("GET", url, headers=headers).json()
        result = response['latestMcSeqno']
        if not result:
            return 0
        else:
            # highest_block = int(block_height())
            current_block = result
            return  current_block


def version():
    command = "console -C /var/ton-work/rnode/configs/console.json  -j -c \"getstats\"|awk -F \"\\t\" \'{print$3}\'"
    process = subprocess.Popen(command,
                                stdin=subprocess.PIPE,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE, shell=True)
    versions = str(process.communicate()).split(",")[3][2:]
    print(versions)
    return versions
def tendermint_info():
        rank = 1
        publickey = "035e5b8af2d5e50c8910c125521d0ca240e98803382851e10cb6ebf4009ed451"
        url = "https://api.everscan.io/v1/elections/state"
        headers = {
        'accept': 'application/json'
        }
        # response = requests.request("GET", url, headers=headers)
        # print(response.text)
        try:
            response = requests.request("GET", url, headers=headers).json()["currentElection"]["members"]
            for rep in response:
                if rep["pubkey"] != publickey:
                    rank +=1
                else:
                    result = {"miss_signed": 0, "miss_block": 0, "jailed": 0, "rank": rank}
                    print(result)
                    return result
        except Exception as e:
            print("ever tendermint_info error: %s" % str(e))
        return None
tendermint_info()
block_behind()
version()