from typing import KeysView
import requests
import json
import xlwt

workbook = xlwt.Workbook(encoding="utf-8")
sheet1 = workbook.add_sheet("coinmarket")

# coin = ["1INCH","AAVE","ACA","ACH","ADA","AGIX","AGLD","AKITA","AKRO","ALGO","ALPACA","ALPHA","ALPINE","AMB","ANKR","ANT","APE","API3","ARDR","ARPA","ASTR","ATOM","AUTO","AVAX","AVXL","AXS","BABY","BABYDOGE","BADGER","BAKE","BAL","BAND","BAT","BCH","BETH","BICO","BIT","BNB","BNC","BNT","BNX","BORA","BORING","BP","BSV","BSW","BTC","BTM","BTT","BTTC","BURGER","BZZ","C98","CAKE","CEL","CELO","CELR","CELT","CFX","CHESS","CHR","CHZ","CLV","COMP","CONV","COTI","CPOOL","CQT","CRO","CRV","CSPR","CUBE","CUSD","CVC","DAI","DAR","DASH","DATA","DC","DCR","DFI","DNT","DOCK","DODO","DOGE","DOME","DORA","DOT","DYDX","EFI","EGLD","ELF","ENJ","ENS","EOS","ETC","ETH","ETHW","EURT","EVMOS","FET","FIDA","FIL","FITFI","FLM","FLOW","FLUX1","FORTH","FTM","FTT","GALA","GAS","GEEQ","GF","GLMR","GMT","GNO","GODS","GOG","GRT","HAKA","HBAR","HC","HELMET","HIGH","HIVE","HNT","HT","HYDRA","ICP","ICX","IDEA","IDEX","ILV","IMX","INT","IOST","IOTA","IOTX","IXS","JASMY","JOE","JST","KAR","KAVA","KEY","KISHU","KLAY","KMA","KNC","KSM","LAMB","LAT","LEVER","LING","LINK","LIT","LOKI","LON","LOOKS","LOOM","LPT","LRC","LTC","LUNA","LUNC","MANA","MASK","MATIC","MBOX","MC","MDX","MELOS","METIS","MINA","MJT","MKR","MOVR","MTL","NAS","NEAR","NEBL","NEO","NFT","NKN","NMR","NUM","NYM","OGN","OKB","OLT","OMG","ONE","ONG","ONT","OOKI","OP","OPUL","OUSD","PCX","PEOPLE","PERP","PHB","PHNX","PIVX","PNT","POLYX","PROS","PSL","PSTAKE","PUNDIX","QKC","QNT","QTUM","RACA","RAD","RARE","RAY","REEF","REN","RIF","ROSE","RSR","RSS3","RVN","SAND","SANTOS","SC","SCRT","SD","SHIB","SIGN","SKL","SLP","SNT","SNX","SOL","SOS","SPA","SPELL","SRM","SSV","STARL","STETH","STG","STMX","STORJ","STRP","STX","SUSHI","SWEAT","SWRV","SYLO","THETA","TOKO","TOMO","TORN","TRB","TRX","TT","TUP","TUSD","UMA","UMEE","UNB","UNFI","UNI","UNO","USDC","USDD","USDT","VAI","VELO","VET","VIB","VISION","VSYS","WAN","WAVES","WBTC","WEST","WIN","WNCG","WNXM","XAUT","XCH","XEC","XEM","XLM","XMR","XPRT","XRP","XTZ","YFI","YFII","YGG","ZBC","ZEC","ZEN","ZIL","ZRX","TRUE"]
coin=["ETH","BTC","MELOS","USDT","VISION","UNO","PSL","TOKO","HAKA","VAI","HYDRA","PHNX","MJT","UNB","XPRT","IDEA","TT","NUM","USDD","DFI","IXS","GEEQ","USDC","ATOM","DOT","LUNA","MATIC","NEAR","ZIL","KSM","OPUL","OLT","CPOOL","ADA","FTM","BNB","SOL","VSYS","TOMO","WAN","ONE","TRX","LOOM","WAVES","XTZ","DCR","PIVX","IOST","IOTX","OUSD","WEST","LOKI","ALGO","HT","SYLO","SIGN","CUBE","KMA","AXS","POLYX","CUSD","BTT","EVMOS","SCRT","BICO","CRO","ELF","AVAX","FIL","SUSHI","ETHW","STETH","DOGE","SHIB","DC","CAKE","LOOKS","DASH","ETC","BIT","IDEX","MDX","ILV","BABY","GALA","HELMET","YGG","DYDX","BNX","RAD","PCX","SPA","AVXL","CHESS","BNC","BP","RACA","FLOW","RARE","AGLD","STRP","BETH","FLUX1","STARL","NEBL","THETA","ACA","LEVER","BURGER","STX","SKL","MINA","NKN","KAVA","SAND","ACH","CELR","BTTC","GLMR","NEO","REEF","BSW","AMB","LIT","QTUM","EGLD","ONT","ICP","OGN","ROSE","EOS","BAKE","DODO","DAR","HIGH","CRV","GRT","MC","STMX","VET","MOVR","CELO","DOCK","ARPA","RAY","FET","ALPHA","CHR","HNT","KLAY","LPT","1INCH","ANKR","COTI","FORTH","GAS","GMT","GNO","MTL","PHB","PNT","PROS","QKC","SNT","SNX","SSV","LUNC","STG","UNFI","VIB","WNXM","AKRO","ALPACA","ALPINE","ARDR","AUTO","BCH","C98","CHZ","DATA","DNT","FIDA","FLM","FTT","HIVE","ICX","IOTA","JASMY","KEY","MBOX","NMR","ONG","OOKI","OP","PUNDIX","QNT","RIF","RVN","SANTOS","SPELL","STORJ","XEC","ZEN","ZRX","AGIX","API3","BADGER","SOS","LING","ZBC","BORA","BNT","BAND","MKR","METIS","UMA","CSPR","NFT","GF","VELO","LAT","XAUT","JOE","LON","EURT","SWEAT","INT","LTC","XRP","CLV","BABYDOGE","MANA","PEOPLE","PSTAKE","SD","DAI","TUSD","KISHU","APE","RSR","NYM","FITFI","ZEC","LAMB","UNI","HC","OMG","EFI","XMR","XEM","BTM","LRC","SLP","WNCG","AAVE","LINK","BSV","KNC","CVC","XLM","GODS","IMX","ENS","NAS","CFX","TORN","MASK","PERP","SC","ANT","JST","DORA","CONV","ENJ","ASTR","CEL","COMP","BAT","XCH","DOME","OKB","HBAR","BAL","RSS3","REN","UMEE","SRM","AKITA","YFI","YFII","TRB","SWRV","CQT","BZZ","KAR","WBTC","TUP","CELT","BORING","GOG","TRUE","WIN","USDG","XELS","REDTOKEN","CMP","MPLX","PORTX","LGX","BVT","ITSB","GT","SHX","BDX","MBL","LEMN","MLS","ETHF","DDOS","CRPT","FXS","FARM","FEVR","B3X","VINU","SKEB","WING","WLKN","SWP","ITEM","RARI","MFT","RBLS","MNZ","MOB","DREP","FOR","PLA","TKO","POLY","DF","AUCTION","GRND","TARA","CKB","PET","MLN","STAR","DVI","FIS","MBX","OM","IDV","PROPS","VGX","QUICK","AZY","GAL","NXD","CUP","TIPS","COOK","BAS","SQUIDGROW","TOMS","CHO","ELT","BENQI","REQ","BOND","GRIN","HMT","BLES","TWT","ASD","ATA","VOXEL","IRIS","SHFT","VVS","MIR","BLZ","AIOZ","NEXO","RAI","SXP","MAPS","XVS","SUKU","XCN","ALICE","AVA","DOG","KDA","XPR","WEMIX","CWEB","HEGIC","WICC","WSIENNA","GTC","CTK","SLIM","CART","WOZX","VIDY","KAI","ALCX","DENT","CRU","NBS","HAI","BAC","ASR","SAFEMARS","PIG","T","VRA","DOGGY","SYS","POLS","BTCST","SCLP","SPI","BEAM","LION","ALN","BCD","POLC","AUDIO","WAXP","WXT","MTRG","PYR","PHA","JULD","SPS","PEARL","AERGO","XYO","O3","LEMD","CRP","HOT","RLY","DAO","INSUR","LOKA","ERN","JGN","EPK","LEO","TLM","TRU","BLOK","ATP","ISP","SDAO","SUNNY","ASM","MDA","YIELD","DIA","FRONT","FLOKI","PMON","BOSON","LSS","WSG","SERO","FLY","LINA","AR","ANC","ARES","BTS","XYM","TIDAL","CNNS","FIC","RNDR","WHALE","OCT","HAPI","DEGO","EDEN","OCN","AE","QRDO","FIRO","OMI","GHST","SWASH","FEG","WIKEN","KIN","ERG","WOO","KIMCHI","CEEK","WRX","SDN","YAM","ATLAS","GST","GM","WILD","GARI","ZKS","TONCOIN","HERO","TRIBE","LDO","EGS","CYS","MXC","KONO","SUPER","OXY","OCEAN","FLUX","MTV","QUACK","RLC","HORD","POND","SUN","RFOX","ELON","ANML","CTX","NULS","STRAX","STR","TVK","UTK","VTHO","INJ","LTO","TCT","BAO","FRA","HIT","ZEE","PRQ","FTI","FUN","RUNE","NEST","XVG","PERL","OXT","MITH","CTSI","FEI","RAMP","OKT","USDTEST","TFUEL","CERE","USD"]
# coin=["MELOS","PSL","HAKA","MJT","IXS","LOKI","POLYX","EVMOS","ETHW","STETH","DC","AVXL","BETH","FLUX1","BTTC","IOTA","LING","EURT","BABYDOGE","SD","KISHU","NYM","FITFI","DOME","UMEE","AKITA","CELT","BORING","USDG","XELS","REDTOKEN","CMP","MPLX","PORTX","LGX","BVT","ITSB","BDX","LEMN","MLS","ETHF","B3X","SKEB","WLKN","ITEM","RBLS","MNZ","GRND","PET","MBX","NXD","CUP","BAS","SQUIDGROW","TOMS","CHO","ELT","BENQI","HMT","BLES","DOG","CWEB","WSIENNA","CART","SAFEMARS","PIG","SCLP","SPI","LION","POLC","MTRG","PEARL","LEMD","SUNNY","FLOKI","FLY","CNNS","OMI","FEG","GM","TONCOIN","EGS","ANML","OKT","USDTEST","USD"]
url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"

headers = {
  'Accept': 'application/json',
  'X-CMC_PRO_API_KEY': '373711c1-8dfb-45c8-8fa2-fc630f8cd861',
  'Content-Type': 'text/plain'
}
parameters = {
  'start':'1',
  'limit':'5000',
  'convert':'USD'
}
response = requests.request("GET", url, headers=headers,params=parameters)
ALLdata = response.json()["data"]
# print(ALLdata)
dir = {}
num=0
for data in ALLdata[::-1]:
    curren = data["symbol"]
    price = data["quote"]["USD"]["market_cap"]
    if price == 0:
        price = data["self_reported_market_cap"]
    dir[curren]=price
    num+=1
print(dir)
print(num)
row = 0
column = 0
for co in coin:
    currency = co
    if co in dir.keys():
        allprice = dir[co]
    else:
        allprice = "null"
    # print(currency,allprice)
    sheet1.write(row, 0, currency)
    sheet1.write(row, 1, allprice)
    row += 1
    column += 1

workbook.save("coinmarket.xls")