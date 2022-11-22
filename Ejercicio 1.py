#Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'},
#pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está
#en el diccionario.

variable = {"Euro":"€", "Dollar":"$", "Yen":"¥"}
divisa = input("Introduce una divisa:\n")

if divisa in variable:
    print(variable[divisa])
else:
    print("No tengo la divisa", divisa)
