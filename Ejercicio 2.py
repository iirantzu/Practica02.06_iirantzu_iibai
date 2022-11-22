#Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario.
#Después debe mostrar por pantalla el mensaje “<nombre> tiene <edad> años, vive en <dirección> y su número de
#teléfono es <teléfono>”.

nombre = input("Introduce tu nombre:\n")
edad = input("Introduce tu edad:\n")
direccion = input("Introduce tu dirección:\n")
telefono = input("Introduce tu número de teléfono:\n")

diccionario = {"nombre": nombre, "edad": edad, "direccion": direccion, "telefono": telefono}

print(diccionario["nombre"], "tiene", diccionario["edad"], "años, vive en", diccionario["direccion"],
      "y su número de teléfono es", diccionario["telefono"])