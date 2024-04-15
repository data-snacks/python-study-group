from math import pow
#print("Hello World")


numeroEntero =  2
numeroFlotante =  1.5
falso = False
verdadero = True

# print(nombre[1])
# print(nombre[-1])

# for i in nombre:
#     print(i)

print(pow(numeroEntero,3))

def imprimime_juan():
    letra='-'
    nombre = "Juan"
    indice = 0
    while letra != 'n':
        letra = nombre[indice]
        if letra != 'a':
            print(letra)
        indice += 1

imprimime_juan()