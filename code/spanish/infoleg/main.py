#from utils import *

import requests


    
if __name__ == "__main__":
    #test_virtual_env()
    print("Main Program")
    url = "http://servicios.infoleg.gob.ar/infolegInternet/anexos/395000-399999/395521/norma.htm"
    r = requests.get(url)
    print(r.text)
    #print(coinbase_greeting())
    #print(request_text_content_btc())
    #pprint(request_text_content_eth())