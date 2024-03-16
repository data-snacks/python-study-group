# Basic
1. Desarrolla un programa que solicite al usuario que ingrese su nombre. El programa debe emitir un mensaje de bienvenida que incluya el nombre ingresado.

1. Crea un programa que permita ingresar 3 notas correspondientes a tres trimestres distintos para un alumno de nivel secundario. Debe calcularse y mostrarse la nota promedio.

1. Escribe un programa que permita ingresar un número entero. Debe mostrarse el número ingresado multiplicado por 5 y dividido por 2.

1. Elabora un programa que solicite ingresar el valor monetario de una hora de trabajo y la cantidad de horas trabajadas por día por un trabajador. Debes mostrar el valor del salario semanal, sabiendo que trabaja todos los días hábiles y la mitad de las horas del día hábil los sábados. (Todas las horas valen lo mismo.)

1. Crea un programa que permita ingresar valores del mismo tipo para las variables num1 y num2. Una vez ingresadas, mostrar ambas variables por pantalla, intercambiar sus valores y mostrarlas actualizadas.

1. Realiza un programa que solicite ingresar el monto total de las ventas realizadas por un vendedor durante el mes, quien tiene un sueldo fijo de 44000 pesos más el 16% del monto total vendido. Con estos datos, calcula y muestra el importe a cobrar por el vendedor.

1. Escribe un programa que solicite ingresar el ancho y el largo de un terreno en metros, así como el valor del metro cuadrado de tierra. Debe mostrarse el valor total del terreno y la cantidad de metros de alambre necesarios para cercarlo completamente a tres alturas distintas.

1. Crea un programa que permita ingresar dos números naturales. Debe mostrar los resultados de las 4 operaciones matemáticas básicas con los números ingresados.

1. Desarrolla un programa que solicite ingresar dos números que representen las medidas en grados de dos ángulos interiores de un triángulo. A partir de estos valores, muestra el valor en grados del ángulo restante. Recuerda que la suma de los ángulos interiores de un triángulo es 180°.

1. Crea un programa que resuelva el siguiente problema: Tres personas aportan diferentes capitales a una sociedad y desean conocer el valor total aportado y el porcentaje aportado por cada una (indicando nombre y porcentaje). Solicita la carga por teclado del nombre de cada socio y su capital aportado, y a partir de esto, calcula e informa lo requerido previamente.

1. Desarrolla un programa que realice un "desplazamiento" de variables, es decir, que intercambie el valor de dos variables. Esto quiere decir que se va a tener una variable valor_1, y otra con valor_2 y se deben intercambiar sus contenidos. USAR variable auxiliar. El programa debe solicitar al usuario que ingrese dos valores y luego mostrar los valores intercambiados.

1. Desarrolla un programa que realice un "desplazamiento" de variables, es decir, que intercambie el valor de dos variables. Esto quiere decir que se va a tener una variable valor_1, y otra con valor_2 y se deben intercambiar sus contenidos. NO variable auxiliar. El programa debe solicitar al usuario que ingrese dos valores y luego mostrar los valores intercambiados.

## Cadena de caracteres

1. Escribe un programa que tome una cadena de texto y la imprima en mayúsculas.
1. Escribe un programa que tome una cadena de texto y cuente cuántas vocales contiene.
1. Escribe un programa que tome una cadena de texto y cuente cuántas palabras contiene.
1. Escribe un programa que tome una cadena de texto y reemplace todas las vocales con un guion bajo ("_").
1. Escribe un programa que tome una cadena de texto y cuente cuántas veces aparece una palabra específica en ella.
1. Escribe un programa que tome una cadena de texto y la imprima al revés.
1. Escribe un programa que tome una cadena de texto y elimine todos los espacios en blanco.
1. Escribe un programa que tome una cadena de texto y la divida en una lista de palabras.
1. Escribe un programa que tome una cadena de texto y cuente cuántos caracteres no alfabéticos contiene.
1. Escribe un programa que tome una cadena de texto y la convierta en una lista de caracteres.
1. Escribe un programa que solicite al usuario ingresar una cadena y una subcadena, y luego determine si la subcadena está presente en la cadena ingresada.
1. Desarrolla un programa que tome una lista de palabras y una palabra de búsqueda, y muestre todas las palabras de la lista que contienen la palabra de búsqueda como subcadena.
1. Crea un programa que solicite al usuario ingresar una cadena y luego muestre la cadena invertida.
1. Escribe una función que tome una cadena como argumento y devuelva True si es un palíndromo (es decir, si se lee igual de adelante hacia atrás que de atrás hacia adelante), y False en caso contrario.
1. Desarrolla un programa que solicite al usuario ingresar dos cadenas y luego determine si son iguales o no.
1. Escribe una función que tome dos cadenas como argumentos y devuelva True si son anagramas (es decir, si contienen las mismas letras en diferente orden), y False en caso contrario.

## Listas
1.
lista = ['Alicia', 1998, 'Bob', 1990, 'Carlos', 1986, 'David', 2001]
Question 3
Tienes la siguiente lista con nombres de clientes y sus años de nacimiento.
Quieres imprimir el nombre de cada cliente seguido de su año de nacimiento, por ejemplo, para la lista anterior quieres imprimir:

Alicia 1998
Bob 1990
Carlos 1986
David 2001

 1.
lista = ['Alicia', 'Bob', 'Carlos', 'David']
Quieres imprimir el nombre de los clientes de atrás hacía adelante, por ejemplo, para la lista anterior deberás imprimir:

David
Carlos
Bob
Alicia

1.

m = ['Pelusa', 'Luke', 'Mickey', 'Madonna']
El dueño en la posición 0 tiene la mascota en la posición 0, el dueño en la posición 1 tiene la mascota en la posición 1 y así. Quieres imprimir el nombre de cada cliente dueño seguido del nombre de su mascota, por ejemplo, para las listas anteriores quieres imprimir:

Alicia Pelusa
Bob Luke
Carlos Mickey
David Madonna

1. 
Tienes una lista con datos de una estación meteorológica, esta contiene los strings 'soleado', 'nublado' o 'lluvia'. Siempre después de lluvia viene un float con la cantidad de milímetros de agua que cayeron durante la llovizna. Un ejemplo de esta lista es:
lista = ['soleado', 'nublado', 'soleado', 'lluvia', 2.4, 'lluvia', 0.1, 'nublado', 'lluvia', 0.8]
¿Cuál de los siguientes códigos imprime la suma total de milímetros de agua que cayeron?

## Tuplas

1.

def imprimir_hora(mes,dia,hora,minuto,segundo):
    print('Hoy es '+ str(dia)+ ' de ' + str(mes) + ' y son las:')
    print(str(hora) + ':'+str(minuto)+':' + str(segundo))

No te gusta que la función anterior reciba tantos parámetros, por lo que decides entregarlo simplemente una tupla con toda la información.

1.

m1 = ('Toy Story', 1995, '01:21', ['animacion', 'comedia’])
uego de hablar con tu agente te recomienda que agregues a la lista de categorías la categoría infantil. ¿Cuál de los siguientes códigos agrega correctamente la categoría?

1.
El profesor acaba de volver a corregir las notas y tu nota en la primera evaluación subió de 2.0 a 3.2. Como sabes que las tuplas no son mutables decides pasar todas tus notas a una lista y reemplazar el 2.0 por el 3.2. ¿Cuál de los siguientes códigos hace lo pedido correctamente? 

1.

clientes = ['Alicia', 'Bob', 'Carlos', 'David']
clientes_nuevos = ('Eva', 'Fabricio', 'Gloria')
Quieres agregar todos los clientes de la tupla clientes_nuevos a la lista clientes ¿Cuál de los siguientes códigos lo hace correctamente?

1. 

tupla = (0,1,2,2,2,4,2,1,2,4,4,4,0,0)
Necesitas ordenar los valores en la tupla, para esto decides crear una lista y luego agregar en orden los números en la tupla. ¿Cuál de los siguientes códigos hace lo pedido correctamente?

# Tipo de datos y condiciones

# Repeticiones

# Clásicos y famosos

## Algoritmos de búsqueda:

1. Búsqueda lineal.
1. Búsqueda binaria.

## Algoritmos de ordenamiento:

1. Ordenamiento burbuja
