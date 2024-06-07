from coinbase_request import *
from coinbase_get_time import *
import time
from datetime import datetime
import json
    
if __name__ == "__main__":
    cotizaciones = []
    cantidad = int(input("Cantidad de peticiones: "))
    for n in range(cantidad):
        data = request_text_content_btc()
        data_lista = data.split('":"')[1]
        amount = float(data_lista.split('"')[0])
        print(amount, type(amount))
        cotizaciones.append(amount)
        #time.sleep(2)
    print(cotizaciones, type(cotizaciones))
    set_cotizaciones = set(cotizaciones)
    print(set_cotizaciones, type(set_cotizaciones))
    data_time=get_time()
    print(data_time)
    data_time_text = data_time.split('":"')[1]
    print(data_time_text)
    data_time_text = data_time_text.split('"')[0]
    print(data_time_text)
    datetime_object = datetime.strptime(data_time_text, '%Y-%m-%dT%H:%M:%SZ')
    print(datetime_object)
    print(datetime_object.year)
    print(datetime_object.month)
    print(datetime_object.day-1)
    print(datetime_object.weekday())
    tt = datetime_object.timetuple()
    for it in tt:   
        print(it)
    data_time_json=json.loads(data_time)
    print(data_time_json['data']['epoch'])

    