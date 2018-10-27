import json
import urllib.request
from urllib.request import Request, urlopen

class bithumb:
    urlTicker = urllib.request.urlopen('https://api.bithumb.com/public/ticker/all')
    readTicker = urlTicker.read()
    jsonTicker = json.loads(readTicker.decode('utf-8'))
    FindBTC = jsonTicker['data']['BTC']['closing_price']
    BTC = int(FindBTC)
    FindETH = jsonTicker['data']['ETH']['closing_price']
    ETH = int(FindETH)
    FindDASH = jsonTicker['data']['DASH']['closing_price']
    DASH = int(FindDASH)
    FindLTC = jsonTicker['data']['LTC']['closing_price']
    LTC = int(FindLTC)
    FindETC = jsonTicker['data']['ETC']['closing_price']
    ETC = int(FindETC)
    FindXRP = jsonTicker['data']['XRP']['closing_price']
    XRP = int(FindXRP)

class coinone:
    urlTicker = urllib.request.urlopen('https://api.coinone.co.kr/ticker/?currency=all')
    readTicker = urlTicker.read()
    jsonTicker = json.loads(readTicker.decode('utf-8'))
    FindETC = jsonTicker['etc']['last']
    ETC = int(FindETC)
    FindBTC = jsonTicker['btc']['last']
    BTC = int(FindBTC)
    FindETH = jsonTicker['eth']['last']
    ETH = int(FindETH)
    FindXRP = jsonTicker['xrp']['last']
    XRP = int(FindXRP)

class korbit:
    reqBTC = Request('https://api.korbit.co.kr/v1/ticker?currency_pair=btc_krw' , headers={'User-Agent': 'Mozilla/5.0'})
    readBTC = urlopen(reqBTC).read()
    jsonBTC = json.loads(readBTC.decode('utf-8'))
    FindBTC = jsonBTC['last']
    BTC = int(FindBTC)
    reqETH = Request('https://api.korbit.co.kr/v1/ticker?currency_pair=eth_krw' , headers={'User-Agent': 'Mozilla/5.0'})
    readETH = urlopen(reqETH).read()
    jsonETH = json.loads(readETH.decode('utf-8'))
    FindETH = jsonETH['last']
    ETH = int(FindETH)
    reqETC = Request('https://api.korbit.co.kr/v1/ticker?currency_pair=etc_krw' , headers={'User-Agent': 'Mozilla/5.0'})
    readETC = urlopen(reqETC).read()
    jsonETC = json.loads(readETC.decode('utf-8'))
    FindETC = jsonETC['last']
    ETC = int(FindETC)
    reqXRP = Request('https://api.korbit.co.kr/v1/ticker?currency_pair=xrp_krw' , headers={'User-Agent': 'Mozilla/5.0'})
    readXRP = urlopen(reqXRP).read()
    jsonXRP = json.loads(readXRP.decode('utf-8'))
    FindXRP = jsonXRP['last']
    XRP = int(FindXRP)
