#Escribir un programa que cree un diccionario de traducción español-inglés. El usuario introducirá las palabras
#en español e inglés separadas por dos puntos, y cada par <palabra>:<traducción> separados por comas, hasta que
#el usuario introduzca la palabra “terminar”. El programa debe crear un diccionario con las palabras y sus
#traducciones. Después pedirá una frase en español y utilizará el diccionario para traducirla palabra a palabra.
#Si una palabra no está en el diccionario debe dejarla sin traducir.

traductor = {}
palabras = input("Introduce una lista de palabras en Español y la traduccion en Inglés separados por una coma, "
                 "EJEMPLO: Hola:Hello,mi:my,nombre:name,es:is,Irantzu:Irantzu. \n")

for i in palabras.split(","):
    clave, valor = i.split(":")
    traductor[clave] = valor
frase = input("Escribe una frase en Español: \n")
for i in frase.split():
    if i in traductor:
        print(traductor[i], end=" ")
    else:
        print (i, end=" ")

