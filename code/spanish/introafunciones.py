print("intro a funciones")

nombre = input("Decime tu nombre: ")

def imprimir_nombre(x:str):
    print("Vos sos bienvenido:", x)

imprimir_nombre(nombre)
import math 

input_base = int(input("Base: "))
input_exponente = int(input("Exponente: "))

def exponencial(base, exponente):
    resultado = math.pow(base, exponente)
    print(resultado)

exponencial(input_base, input_exponente)

from datetime import datetime
print(datetime.today().strftime('%Y-%m-%d'))
print(type(datetime.today().strftime('%Y-%m-%d')))
print(datetime.today(), type(datetime.today()))