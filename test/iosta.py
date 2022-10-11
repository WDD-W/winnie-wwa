import requests
import json
import xlwt
def export_excel():
    workbook = xlwt.Workbook(encoding="utf-8")

    sheet1 = workbook.add_sheet("sheet1")

    sheet1.write(0, 0, "hash")
    sheet1.write(0, 1, "数量")

    items = claimed_reward()
    row = 1
    for item in items:
        sheet1.write(row, 0, item['trx'])
        sheet1.write(row, 1, item['mount'])
        row += 1

    workbook.save("iost.xls")
def claimed_reward():
    mount_list = []
    iosttrx=["AZmEEYzQY9QroeYHhavykkHb6sWeJsJePzzV3A4Xd6ix","GEd9UXu9hwW21qeTH5EpshmfXfAqd9LBdfE9ukqyhyHz","56H5uDybTbUDoJfmUnDQJkpGmYt4EGPNjcmMmeDyxweB","FicCaeojrs4WTQhUzGEJC1zUyttW4PT1RXbRdUVuAg17","C6rSo4RpiXYRtaW1rke87Hb81Pd4WssDzjRk1RXy18bj","1VcS6ZpQYnVk8S1vVnwMdDVSsZ7fcecoTZnh683QgZH","CRHu4Ubcae3rKdnvxEVhpWbGjswtrwggH5aUzYJzaQxU","8uiLHVza98cTTNBvNadtgxEUHzvxHPWSpmiQgcodyXM6","HnkQ5hSRv8WU1SXZbK564wzZopnJzxSV7xqxuV9H2mNe","7RhK8hNPhGfvQm6ZBGhvk8Uhsv24mcnrrpVzVjxt96xq","GEVPVZFtmqiQm9McEdqjiaQ2KqaUjkPXE18bjuESDeaK","8SKQLQmbkZfN6AEfpG2fx8SQYnjxCxXKSzLSyF6kMHoX","HEEAakE5kdjPvZhaifwvSxZJ3rgyqHc8UknoMuoHipy8","FNhXSExVX2RdNzqFBuTXLSCjtAYRDX42C35TPWK7z77M","J9VXm9PFtToGKmeLahHj3Ct4enTqJ1Vu4XCy7ZxebNhL","FTBbQu3wfwqPdNrd7t2wc1sDJjNNR3u2tqSJuEY6QRjv","61X3iApxLedPtKpiyZhKHPKbRF3U1Ggc8YvCLdGqEhnF","DnA3AtXRKKZsVebNLwxqnmMtChP4M2DY5NCjxz9friUp","BWm6VkQ4ajccei7KkB3d9BrKLJG43bTUVkTkkMX4w577","24vbdxYrPtWJgpTGWuQJqDFgPwnLKHwrrFLdwuhFtwhN","AeJT9nqDtGGQQzV4in9JLc7FkVk4o4G496cxVbKgxeg1","5DTfRC6jN4GB6AGbJN9ygXGpSS3w7VgHcj1HjEamgGF4","BPapXH3DLPhfsUEwtyKwKSJWgz8JFmseBh6erwECfFPT","GiCtUbnziBhuRPk3oBo7bZoBMcw7x4opNMTs1QbUZAnt","9Lb85oHvr38sAobZ9wQ1TvA2aUNr6KDoKmWWjC4EMo7h","C6Kjyt1aoAjGeQDpLUqt7QK3zCrCMKmWUmswuPYoiL23","CcEZ9ieSsxE3MDMUN22aw89ZarUmn6c7DC1cFoh7dc2h","6Q9ZpUzu3buthYM9W8Lu4BcoEcYSpZXxNH867SMWDjQU","DpvZNjuarQFF5LRx2FfU5Fo8C2TpYQbrBiEqpKK3RLbK","86yNzidWuFUSiHkAqmMiWduKW2D9VohNAHcRY4ekHmwr","6PLj5YhoHT21UU1S8pcE9pxPB5rFoUjUiKBtMGhqsCw3","E3mU6NEVRcwPNRbxFA6RRVNi1ezWUjvbt8xddrwty856","49h4ptWx77gWj1H1wcTPEmf5fMwXMjqnhfwfK73ThkZf","5MjY1VCHzh59bv3jc34nMUE9GsdSDAvGFhQ7hqiBXecP","5QkdudPXbwue83CX4DS6MAesWShsK7forhtGsHm6VGzv","3M6Za9DuuwPYTeDGG9Ja6C7j9DfyzXscYB1CUkeMzGB9","GvTzeCmFLsakcFMwFDB1gMZXdvH4WPUN4jFKKboFhwBR","BtPdjDZhPZm7axNEJS6otfJ9drnk62awdLvfJMcbtqqD","J26Z4M1Naa7LX7bX3aJfCDNBp5eEmipoVT7MCpTL79FD","8ZGwPY4cMqqbykQ34n1RR4sSi77dHLc4CrQZfdtvQnWQ","8uDGRBPEPrMUT4DDvnhiqpp7XLNi2F6AidYwaULzkdH5","GimpcefH7GQgDGYTz445HoqsrTtMH7DxRKH3voqMUkcy","3ZfgRsAi3bsc9SQ6XevZmqyQ6LbWmev7cT4WiyisRUC4","6dkkAvztgRciamKJZgT23P4Jzj17Mhsi82BYgtzZ4RrB","9XG2zeQuY7q5pZmuztAW1CjXesNcbhKy1SyddvidkCGn","Gy4uJwZBz8pz3TvKbuRa6GGSDYJxr2v2ZhQe6hPJMzr4","8XMuLLFSvX9tmHPF2ZTv9k8jDVfR7hASNVq384Xi12RN","Hn1f1wKGYXtqoSDCSKPEerMhQDMH1nBA8BMrhzaDZbvG","DUEY4VeqUYtWNCtAKpegzietgtRRsSU7uevxB7uQcJso","H8uYLNChLKVngU7ftThsnunohRHBWoY5A4FDZMUmWtxd","AhM7bAFXZqMXfjZ44mCtmSi3xFiqFrofQRS2JtHrZd5P","2NhiucyXnpMAAnzUrPmhW1kqkJv3kdCYsANGeBxpjLRD","H9kUVn4QMCW3Dp4Qf3RPQmzpNSaUb4X54jXDLni5TSoe","Dm3XwZNorq3Xn9FK7ya1f1PFxiF4Lp2WAr8UC8EFiPdv","2qGRS75RtXE9RJncvFYzver2Ze3kHm348tYCHg9zCLNt","BU6dtwaGT2qLRS9mVE9h8Wfv8h7Dpthp1h9HSUnjuD1i","3uTQsRMWs8SHQLeF7JPDrhVfM4azP2kMEZDw96DZ3NRD","5g2w9Q3Bk1BMgjNrV3dBeAW7PcuMVnQSiRWKZj3qSKMJ","DXVNQsKKBSPa5bwFUBb16DpjPGq38dXJH1Q7Zafv7uiw","26C4LGgFBtNk6sbLPF6MHoQZGQeGUjNhkdhEiZEzqmTP","84Px8ieS3VrgUQ6rXEQ1eb9fqJF8qPP9Vu7PH2XC8DKz","CXsoEG5oYRMX4idquuiZUieuc2tSeXy8MyGNf1qo3WRm","6T9Ubj69qYKqKuvrcSx9WnTCn7CAn6XbW6eUZAnR1Y8j","E1nVvasnasy1hYqYcoqamBdXVYKkG25oVsV9qxbxP6uR","7wRSG26U2cGU4tQ4dFqoLpokbUE2WxtWNpRYKxXGiW1B","GBqCEReeBchjUiD9U9DvMteBPKkN1NsbPwDow7n3zi6D","KfvHCK7xuNBTce4npE4QopBi7rnY4WisFYMoEVRUySJ","DeR3jyHSQC8L4huahp6b1e4Fx8gmWatD5WiFdd7LfTbX","2XWDoCG8ewBcCWM3Rh95vfSi1VUUhQC5mHJM3Es6hgwi","V9J7FsNaZJMkBKWQbhbK1sR1L9cvCNAuk3fXkMqexFw","9HAhmdyeaZfjbPhe7pmGJFoT4yhMsVcRt2w12g9GmGtv","2PqXVygdXGEDtxLBVw5Y3rXEis9kmE5Fd9zTaRXLtLPU","47bfyQ5Bc12BjdSZCyx42aLJi2DXD9NKuJjaKVx2W6V5","5VXDMkhcmJdNeBniRbTSiW4utKwMEnYxF8tWj7xaQuHp","wZVgWvPp2PZibQUFcYTb2zdXVeqnKFjFUfNAFFW3L7W","85GhUBYhXuYuxYN2DvxqgCw64dcByUiTTnhqSAPpPW3v","5WKiCU6CkUGsPYwg3jmmCeH9UsHGeTHoibXzBntVLcKn","4BGpWXhjCU9fhtmn5iQL24a2dNGquaEEe3NArF4RRMJb","GYhpyEPdsQKKazs7DrfM2QbE1kTUjVboj4faECmsR5Kz","6Z8FcVDbrBR24YpfxJB7eyQ1u6QdBHJ6vMGnfcH16VyX","6mFqPRXG2BR3zgqoWAxak4LHVkDPAYh2ckRJiLkzXkoB","7hJFX48uSvKxDTMSPCsWwgzsbV9uGu2GwfezgirhMXP6","CJWuLjS7VrZBRCZDGXV2r9bFsQ24gvtVLWuaBqqefkZ2","6c9vb7m1XMGbPRN8hUg51CCbvuFFm5FAHN5YoXTEDLjD","2VPfoKGnzWDJRP5Ttezn6gVvfmrzH6KWkjPjKrU9oibB","839R5ywSzPERFmpDkt9MjLW1X5uibiHShZZRpT4vHvrJ","FC1uozfjDdYwotgXefJuRUsTJ4ngiL4QNferkyEwAx2N","7CvqwRwnpmQA1Kcu3rTy9twkUrExsEFcnmAWoEFRxhKS","G4cU48f4tJsKU7UMjk6Ac3LyJGpGSTLRpuZVuSKuUPJA","Hg9PGM7qbmFBo61X9VvPnzZKUdd8CBdxJHbJ5eMVjSwi","4cbMrPEdwRFBbUfejHqYdiXSQEUQiUonR31JEoMxLvNJ","HWY3UGFKh1ieNVgWKUgXdGbAsdSUKPBc3LwMw1H6hRtD","5SHWURoUeBC6MAVCkVHVaUGKoS8Fu3fYoYDU1LU21H6P","jAu8zDfVhTxNCinw5xWW55PLm5cAGZ2UGgHAQvS3qyY","AkEP8buPs8v4AWVofuAQaBwhZZtNvymFa98QJQTCKgLN","3EPM1spsHiQqvZCTR6qEDSZTv2cc9pSxDpSyax6Yr83L","EZT3Wkc4JvJC815unM5CqBw9fukfufFMtuzhRNMQPpKL","63XLZnvMNDnqJZbPvu2qzWtd4pv2r4gTBoZ1PW6ueVps","DWtMfWU6TmiKLPkBgyg8sQqcXcrCSTnN8G4SRxUdGznS","Cwycb2Wvwuy9XzZRgTvMnWJVjsYf3DpBZBnfqZc2R3dx","Enks3Ne17rgTQjRqvrYSUjbFPjavTBoHtL8JdyvSbJv5","AKdCyhkLKKZCyz1wskUMVsoEEUW1SxcSSCXdU6Fq9rYR","6oUUAYZ7gdqAtx1mSS4e9oPqVTnVKcxkDhvRuLU6rtQG","ENJbcEwy1d6oMmhWXdmumRE6dWfX9caR9Jda2XQKvzrS","F2VZvPgGmVGifZ6bVKrWnwMPRHJNBePYuQZVZrXT2cAm","2PHKkfLTWZteMfxMCDRAS12Btm6v9cU9HTN8tmHo9oa3","5HLtmDk4YgbiMkr78xX9DH8mkXJBifjGwCWnQPzKPyc4","HUwEUeU2DRcuhacqeXcQRr3swPxwaA27yGRJA1ECKTkw","D7BkjaM6FQzDjxNxYvT255xyht17fUKwBzHPamKSdGs4","FUZiZf8jJEPug6y6QUAcyTQVwwFMFFrofmhWFJosTZM1","4SFBqsPSg2YPdmfcwZVmg6X8YzE9p5h6jLCE9hZNURn3","JCh6433R9ujFJ67MQ2L5bNB9YUfcDrGsEYZD2kxqjUC2","Bxunx6iS6nbbtbR8PmXvnbKzuhMC1uPHDuNkExWmJRFA","82ce6s6dhhPxzmpqhPF5Y3FJCtPSrZkT9qq596sWiC2","sozRgzvVyAt6aJP9uZbBZLVceQHznStEQc7yGB4n5HF","9vHHXXcgmPEPfodn9tTERLybkY9ZhvyNbFR9TDNPpyhV","ALr8E497RBoZyu1ZdNayYcSjTNRcMKgdxZ3T8aWfRU4u","5ZxdXhETSMeKB9VnUQzRLHtGGf4jJL1TGCiuWFJnhsSL","8U7SXg72W9zWHH6o1wT85gCTJwwzhub7AJa4dRuNN8eB","7gZR5a9F5Vo7zNDeF3BjhQg4K1T1of6iGU4xMtswEQ9d","8DmgAFcF5AWSAsQCEzUsEcwTzcceuL7RrVoj9W69HnAw","Hyi4rqLziPSd9rScrhSgwWsXpZtV9xZVTNH7SAHj7cGp","41Pdx9Ma8ThZ7j9c14DMez4Uh8EcvNDPpfx9pTPzCLFF","2H3fLVMYDeufen21Q5XjjYsVYt8CcKviCemLw3m19sWj","Fdojju97FFJBr6ajYoXQFkMrWFXEjHhdnLgsPioELyQV","EXL6GL7G5LbZcEf3s2b65PvHKJ95JkyyRDv47L3UWNoY","7JBpWidX9Na8ZZDNgQgnVKwMPCFn7cNk91CM5SfnGho2","9DrEBrgbujvxwXTyyZakwq2YERKGqanyBnkigN9sV5jN","EkV8wVv1UiXBTLPLKfwrpMBYXeJcmu8A1cZzExzr74FH","E6zn2RQ6xG2EKEkvJ1Z9XybPeT6UhwNFdFyusvobkkqn","6eTzk4odtZ237pxNvKYNJB8gqbtWUMob5o9T9yfikYpa","6nZKk6Rwri4TnySDfK253dMchzBerMcEPSSTupmZxvve","4Es3xA3hqXTGYaf6rAR9yTUcxEz3ccrhTsBsZUsRa3Wo","A8GU2Z6Ld9Bfsst73zevrpQzMLXHgabMmDf5ydQycPgx","GVp43GEEmxTdfMAmJnYSiwyDgqmggGytvteMkLCEANU5","9Mjv5WWG82fVuMZDz3tUzTR7u7gYcBXqHWRJCDExC9Mm","A9tvuddnydhexa8x3vkzKb5NzN5Ya2ZnVtUUBNpjQfAc","4wWKCciT3Zjf6xUUc1so5GZwhwsVZy1pm1uaQu5RTu2s","J3ukQTSbgZtoqAtBaMuGjAJ6v3QpysCBhVXFX6WhWTkw","6SsPoz66N1hGphAzBhboa8UBqN2VJsk48BwcuWLVY5PK","6VBLcSx5q2gfUP983U72mhzphPfhGjpNFUZXcTq98usm","9m9mJE5bM8ps9v5biUqzEDeJEqMfuiboMRbWFztgSYVd","CNz3CTs2NdLLaVQP2LP7MDb76sQ3fsLKUn9PsMiorK1j","FdcXKESsbZZ9AiTkqeFEBs4LPNP2wUqRjbBDqHxuLbN","HMC1v82cEzzpjoLg9BDsbBJ6HRtWFF3ZGMJW993PWTkt","4P79xViTaLtcd5t86dsknbQgGqN1MjkPk5dsVaaswMn1","AUGawGwEJDeR46796TMRHERGS3MbYtY1FfrEGFrNW757","FoExGMBkeJH7Vr5jjxK5wNQaBHScRrc2PpEXjCbkAVKK","3pMdK2BHU3kmsLecwvM3DFo1QaFggohX7iU16cB5Vbdu","DAYftcskwcg3FPHaACEmExUN7ahk8HML6d5AFktor52h","7T3TdCBW4if2K4BE9kbnHPw5DbELiAYeTkJqMDnzsKKC","AabpcX8GR4ypJFEx4RFBP2sUfHdhvDtCvXiEP1rQiCyk","CFsBMiwuXFsqWcaWojCuXGFyVsWnij7vFLcJULXLnnWN","9BusXJGAPvghztgKnGPGbBqkHDtHP2MuZbom6V7Xm1Tu","8jnfjgydJfVJ54LfjG43thrnreLzyZGWCYYM18EBzfr9","3yfWVjPkPJjeWaDp8KqYTfkERyjmpU3cWJjAvcXpJb8u","Hmr3vGHkiuagPCL7s14PAd1rhhXhQ4tBc5mpsFDkJytt","ELKf26uDjvsURjhc6gjHVUiDYctuVT9TFggsE2DcgCDt","Cf8Ykm6xqqb6GHW2EABqPN8qbpBxkUUvcgUfAkcUUf7k","EV6MLJkzirDzmAS7W25FQApi9HzGdW4dwYf3UFCvNWWQ","FXReHszJYCKcY7BAZusmQ6KxUEk1JeXyhaPWEMVH6hqr","9VbHGgCH6YTSvxN3wGLynyFDdenXNZNsHJ4V7rdkp12o","BZC8cq8MspdxahRCYdJdC9exo2kEXTrT99MgaR5e9qwP","5fNyAFSuQyvvUNwN8X9rtswqEXSPi5azcvYiLHf27AB9","6UDb6d46Dxo79EBZgn1vLtFYPVuz3hJypWFPYTFm1jXF","CkMZkXJDyyYcD6vWJ7Xv1jVZUYGFsK3TcaHT9LtexfbA","Das8hBTtoSdnYtL63Bc55Y3HoT3q2TLJjP77w7j6XQuB","BRND9qB3M8Fp6gwqFez6XgpbQ5CbVY4yf7arzrMVDQ3b","BwpBEJYhmfQcy9m7P7LmQ7b7Cc7jsCivcAeUjc8aE88","7fK9uXGTwKJFLVizzWpMGZjyuQ6vfiWMwRjnh2XkBJE8","CYj4wy9FCZJoHccv33VhwfrVo31uQgDV2NmZb3dCVrQ6","9rdf6oMNoobYEpfqXBYmuWpwEHhcH1ck5Qt1TbbcbQxf","4GVBqdTWmEJipiS9w8dZjpL1NpCP1XRwSgixjD9LbhmE"]
    for trx in iosttrx:

        url = "https://www.iostabc.com/endpoint/getTxByHash/%s" % trx

        payload = ""
        headers = {
        'accept': 'application/json'
        }

        response = requests.request("GET", url, headers=headers, data=payload).json()
        mount = response["transaction"]["tx_receipt"]["receipts"][0]["content"].split("\"")[3]
        rewards = {"trx":trx,
                "mount":mount}
        mount_list.append(rewards)
        print(trx)
    print(mount_list)
    return mount_list
export_excel()