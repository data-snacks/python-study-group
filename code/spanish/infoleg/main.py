from utils import *
from infoleg_request import *

    
if __name__ == "__main__":
    test_virtual_env()
    texto_ley_1 = request_infoleg("https://servicios.infoleg.gob.ar/infolegInternet/anexos/35000-39999/37048/norma.htm")
    #print(texto_ley_1)
    texto_ley_2 = request_infoleg("https://servicios.infoleg.gob.ar/infolegInternet/verNorma.do?id=395359")
    texto_ley_3 = request_infoleg("https://servicios.infoleg.gob.ar/infolegInternet/verNorma.do?id=395359")
    #print(texto_ley_2)

    leyes = [texto_ley_1, texto_ley_2]
    leyes.append(texto_ley_3)
    # print(type(texto_ley_1))
    # print(type(texto_ley_2))
    # print(type(leyes))
    # for ley in leyes:
    #     print(type(ley))
    # for l in texto_ley_1:
    #     print(l)
    parrafos = texto_ley_1.split("</P>")
    print(type(parrafos))
    for p in parrafos:
        if "Comercio" in p: # Not Contains: https://stackoverflow.com/questions/3437059/does-python-have-a-string-contains-substring-method
            print("Palabra Comercio")
            print(p)
        



