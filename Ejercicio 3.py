#Escribir un programa que guarde en un diccionario los precios de los artículos de la tabla, pregunte al usuario
#por un artículo, un número de unidades y muestre por pantalla el precio de esa cantidad de producto. Si el
#producto no está en el diccionario debe mostrar un mensaje informando de ello.

precios = {"Pan": 1.4, "Huevos": 2.3, "Cebolla": 0.85, "Aceite": 4.35}

articulo = input("Introduzca el articulo que desea:\n")
unidades = int(input("Introduzca el número de unidades que desea:\n"))

if articulo in precios:
    print(unidades, " unidades cuestan ", round(precios[articulo] * unidades, 2))
else:
    print("No esta disponible ese producto")



