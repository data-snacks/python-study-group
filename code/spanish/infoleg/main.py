from utils import *
from infoleg_request import *

#Norma Ejemplo: https://servicios.infoleg.gob.ar/infolegInternet/anexos/35000-39999/37048/norma.htm
    
if __name__ == "__main__":
    test_virtual_env()
    print(request_infoleg())
