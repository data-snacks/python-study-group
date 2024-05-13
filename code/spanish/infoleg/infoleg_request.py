import requests

def request_infoleg():
    url = "https://servicios.infoleg.gob.ar/infolegInternet/anexos/35000-39999/37048/norma.htm"
    r = requests.get(url)
    return r.text