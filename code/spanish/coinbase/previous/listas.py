from ..coinbase_request import *
from ..coinbase_get_time import *
import time

"""
How to run this code. If you have a problem could be realted to the relative imports:
- Got to the root folder -> cd (...)\\data-snacks\\python-study-group\\code
- Run the script as a module -> python -m spanish.coinbase.previous.listas
"""

#20240527
cotizaciones = []
cantidad = int(input("Cantidad de peticiones: "))
for n in range(cantidad):
    data = request_text_content_btc()
    data_lista = data.split('":"')[1]
    amount = float(data_lista.split('"')[0])
    print(amount, type(amount))
    cotizaciones.append(amount)
    time.sleep(2)
print(cotizaciones, type(cotizaciones))
set_cotizaciones = set(cotizaciones)
print(set_cotizaciones, type(set_cotizaciones))