import requests

# def request_text_content_btc():
#     url = "https://api.coinbase.com/v2/prices/BTC-USD/spot"
#     r = requests.get(url)
#     return r.text

# def request_text_content_eth():
#     url = "https://api.coinbase.com/v2/prices/ETH-USD/spot"
#     r = requests.get(url)
#     return r.text

def request_text_content(crypto):
    url = "https://api.coinbase.com/v2/prices/" + crypto + "-USD/spot"
    r = requests.get(url)
    return r.text

def coinbase_greeting():
    return "This is coinbase_request.py"