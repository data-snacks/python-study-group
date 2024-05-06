import requests
import os

url = "https://servicios.infoleg.gob.ar/infolegInternet/anexos/35000-39999/37048/norma.htm"
carpeta = "carpeta_infoleg"

def request_print_context():
    response = requests.get(url)
    # Comprobar que la petición fue exitosa
    if response.status_code == 200:
        # Guardar el contenido en un archivo local en formato texto
        print("Archivo descargado correctamente en formato TXT.")
        return response.text
    else:
        print("Error en la descarga: Código de estado", response.status_code)
        return response.status_code
    
def request_save_context():
    # Crear la carpeta si no existe
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)

    # Realizar la petición GET
    response = requests.get(url)

    # Comprobar que la petición fue exitosa
    if response.status_code == 200:
        # Ruta completa del archivo
        file_path = os.path.join(carpeta, "archivo_infoleg.txt") # carpeta_infoleg/archivo_infoleg.txt
        
        # Guardar el contenido en un archivo local en formato texto
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(response.text)
        print("Archivo descargado correctamente en formato TXT en la carpeta 'carpeta_infoleg'.")
    else:
        print("Error en la descarga: Código de estado", response.status_code)




def infoleg_greeting():
    return "This is infoleg_request.py"

