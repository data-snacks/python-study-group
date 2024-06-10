from coinbase_get_prices import *
from coinbase_get_time import *
import time
from datetime import *
import json

#20240610
if __name__ == "__main__":
    coinbase_datetime = get_time()
    print(coinbase_datetime, type(coinbase_datetime))
    coinbase_datetime_diccionario = json.loads(coinbase_datetime)
    print(coinbase_datetime_diccionario, type(coinbase_datetime_diccionario))
    dia_y_hora = coinbase_datetime_diccionario['data']['iso']
    #YYYYMMDD -> 20240610
    print(dia_y_hora, type(dia_y_hora))
    yyyymmdd_string = datetime.strptime(dia_y_hora, '%Y-%m-%dT%H:%M:%SZ').strftime('%Y%m%d')
    yyyymmdd_datetime = datetime.strptime(dia_y_hora, '%Y-%m-%dT%H:%M:%SZ')
    print(yyyymmdd_datetime + timedelta(days=45), type(yyyymmdd_datetime))