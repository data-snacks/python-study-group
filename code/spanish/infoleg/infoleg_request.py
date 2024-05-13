import requests

def request_infoleg(url):
    r = requests.get(url)
    return r.text