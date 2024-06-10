import requests

"""
    En este Script de Python se encuentran las funciones relacionadas con la 
    API: Time de Coinbase
    URL: https://api.coinbase.com/v2/time
"""
def get_time():
    url = "https://api.coinbase.com/v2/time"
    r = requests.get(url)
    return r.text