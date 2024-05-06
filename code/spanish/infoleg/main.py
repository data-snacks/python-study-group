from utils import *
from infoleg_request import *

import requests

#Norma Ejemplo: https://servicios.infoleg.gob.ar/infolegInternet/anexos/35000-39999/37048/norma.htm
    
if __name__ == "__main__":
    test_virtual_env()
    print("Main Program")
    #print(infoleg_greeting())
    #print(request_print_context())
    print(request_save_context())
