import xlwt
import requests
import json
import xlwt

coin = ["ALGO","EOS","ATOM","TRX","IOST","NULS","TOMO","LOOM","VSYS","WAN","IOTX","XTZ","LOKI","DCR","LUNA","KSM","ZIL","WEST","ONE","WAVES","ADA","DOT","MATIC","XPRT","QTUM","HYDRA","OLT","DFI"]
# coin=["ETH","BTC","MELOS","USDT","VISION","UNO","PSL","TOKO","HAKA","VAI","HYDRA","PHNX","MJT","UNB","XPRT","IDEA","TT","NUM","USDD","DFI","IXS","GEEQ","USDC","ATOM","DOT","LUNA","MATIC","NEAR","ZIL","KSM","OPUL","OLT","CPOOL","ADA","FTM","BNB","SOL","VSYS","TOMO","WAN","ONE","TRX","LOOM","WAVES","XTZ","DCR","PIVX","IOST","IOTX","OUSD","WEST","LOKI","ALGO","HT","SYLO","SIGN","CUBE","KMA","AXS","POLYX","CUSD","BTT","EVMOS","SCRT","BICO","CRO","ELF","AVAX","FIL","SUSHI","ETHW","STETH","DOGE","SHIB","DC","CAKE","LOOKS","DASH","ETC","BIT","IDEX","MDX","ILV","BABY","GALA","HELMET","YGG","DYDX","BNX","RAD","PCX","SPA","AVXL","CHESS","BNC","BP","RACA","FLOW","RARE","AGLD","STRP","BETH","FLUX1","STARL","NEBL","THETA","ACA","LEVER","BURGER","STX","SKL","MINA","NKN","KAVA","SAND","ACH","CELR","BTTC","GLMR","NEO","REEF","BSW","AMB","LIT","QTUM","EGLD","ONT","ICP","OGN","ROSE","EOS","BAKE","DODO","DAR","HIGH","CRV","GRT","MC","STMX","VET","MOVR","CELO","DOCK","ARPA","RAY","FET","ALPHA","CHR","HNT","KLAY","LPT","1INCH","ANKR","COTI","FORTH","GAS","GMT","GNO","MTL","PHB","PNT","PROS","QKC","SNT","SNX","SSV","LUNC","STG","UNFI","VIB","WNXM","AKRO","ALPACA","ALPINE","ARDR","AUTO","BCH","C98","CHZ","DATA","DNT","FIDA","FLM","FTT","HIVE","ICX","IOTA","JASMY","KEY","MBOX","NMR","ONG","OOKI","OP","PUNDIX","QNT","RIF","RVN","SANTOS","SPELL","STORJ","XEC","ZEN","ZRX","AGIX","API3","BADGER","SOS","LING","ZBC","BORA","BNT","BAND","MKR","METIS","UMA","CSPR","NFT","GF","VELO","LAT","XAUT","JOE","LON","EURT","SWEAT","INT","LTC","XRP","CLV","BABYDOGE","MANA","PEOPLE","PSTAKE","SD","DAI","TUSD","KISHU","APE","RSR","NYM","FITFI","ZEC","LAMB","UNI","HC","OMG","EFI","XMR","XEM","BTM","LRC","SLP","WNCG","AAVE","LINK","BSV","KNC","CVC","XLM","GODS","IMX","ENS","NAS","CFX","TORN","MASK","PERP","SC","ANT","JST","DORA","CONV","ENJ","ASTR","CEL","COMP","BAT","XCH","DOME","OKB","HBAR","BAL","RSS3","REN","UMEE","SRM","AKITA","YFI","YFII","TRB","SWRV","CQT","BZZ","KAR","WBTC","TUP","CELT","BORING","GOG","TRUE","WIN","USDG","XELS","REDTOKEN","CMP","MPLX","PORTX","LGX","BVT","ITSB","GT","SHX","BDX","MBL","LEMN","MLS","ETHF","DDOS","CRPT","FXS","FARM","FEVR","B3X","VINU","SKEB","WING","WLKN","SWP","ITEM","RARI","MFT","RBLS","MNZ","MOB","DREP","FOR","PLA","TKO","POLY","DF","AUCTION","GRND","TARA","CKB","PET","MLN","STAR","DVI","FIS","MBX","OM","IDV","PROPS","VGX","QUICK","AZY","GAL","NXD","CUP","TIPS","COOK","BAS","SQUIDGROW","TOMS","CHO","ELT","BENQI","REQ","BOND","GRIN","HMT","BLES","TWT","ASD","ATA","VOXEL","IRIS","SHFT","VVS","MIR","BLZ","AIOZ","NEXO","RAI","SXP","MAPS","XVS","SUKU","XCN","ALICE","AVA","DOG","KDA","XPR","WEMIX","CWEB","HEGIC","WICC","WSIENNA","GTC","CTK","SLIM","CART","WOZX","VIDY","KAI","ALCX","DENT","CRU","NBS","HAI","BAC","ASR","SAFEMARS","PIG","T","VRA","DOGGY","SYS","POLS","BTCST","SCLP","SPI","BEAM","LION","ALN","BCD","POLC","AUDIO","WAXP","WXT","MTRG","PYR","PHA","JULD","SPS","PEARL","AERGO","XYO","O3","LEMD","CRP","HOT","RLY","DAO","INSUR","LOKA","ERN","JGN","EPK","LEO","TLM","TRU","BLOK","ATP","ISP","SDAO","SUNNY","ASM","MDA","YIELD","DIA","FRONT","FLOKI","PMON","BOSON","LSS","WSG","SERO","FLY","LINA","AR","ANC","ARES","BTS","XYM","TIDAL","CNNS","FIC","RNDR","WHALE","OCT","HAPI","DEGO","EDEN","OCN","AE","QRDO","FIRO","OMI","GHST","SWASH","FEG","WIKEN","KIN","ERG","WOO","KIMCHI","CEEK","WRX","SDN","YAM","ATLAS","GST","GM","WILD","GARI","ZKS","TONCOIN","HERO","TRIBE","LDO","EGS","CYS","MXC","KONO","SUPER","OXY","OCEAN","FLUX","MTV","QUACK","RLC","HORD","POND","SUN","RFOX","ELON","ANML","CTX","NULS","STRAX","STR","TVK","UTK","VTHO","INJ","LTO","TCT","BAO","FRA","HIT","ZEE","PRQ","FTI","FUN","RUNE","NEST","XVG","PERL","OXT","MITH","CTSI","FEI","RAMP","OKT","USDTEST","TFUEL","CERE","USD"]
workbook = xlwt.Workbook(encoding="utf-8")
sheet1 = workbook.add_sheet("coin_price")

response = requests.get("https://www.kucoin.com/_api/currency/prices?base=USD&targets=&lang=zh_CN")
data = response.json()
prices = data["data"]
row = 0
column = 0
for co in coin:
    currency = co
    price = prices[co]
    print(currency,price)
    sheet1.write(row, 0, currency)
    sheet1.write(row, 1, price)
    row += 1
    column += 1

workbook.save("staking-profit-currency.xls")

