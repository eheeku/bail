import sys
sys.path.insert(0,'./../bail-lib/')
import price
from time import sleep
while True:
    print(price.bithumb.BTC)
    print(price.coinone.XRP)
    print(price.korbit.ETH)

    sleep(0.5)

