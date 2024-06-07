import requests
# 'https://api.coinbase.com/v2/time'
def get_time():
    url = "https://api.coinbase.com/v2/time"
    r = requests.get(url)
    return r.text