#Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona (por ejemplo
#nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo
#dato debe imprimirse el contenido del diccionario.

persona = {}
añadir = 'Si'

while añadir == 'Si':
    informacion = input("Introduzca información sobre una persona:\n")
    valor = input(informacion + ':\n')
    print(persona)
    añadir = input('Quieres añadir mas informacion (Si/No)?')

