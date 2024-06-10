import requests

"""
    En este Script de Python se encuentran las funciones relacionadas con la 
    API: Prices
    URL: https://api.coinbase.com/v2/prices/
"""
def get_price_btc():
    url = "https://api.coinbase.com/v2/prices/BTC-USD/spot"
    r = requests.get(url)
    return r.text

def get_price_eth():
    url = "https://api.coinbase.com/v2/prices/ETH-USD/spot"
    r = requests.get(url)
    return r.text