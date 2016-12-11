import re

print("Se separará una oración palabra por palabra.")
print("Luego, se unirá, sin añadir espacio entre palabras.")

oracion = str(input("Ingrese la oración: "))

while True:
    metodo = input("Que método desea utilizar, 1 o 2?")

    if metodo == '1':
        # Separar palabras, cada palabra queda en un elemento de una lista
        oracion = oracion.split()

        #Mostrar sin espacio
        for i in range(1,len(oracion)+1):
            print("La palabra {0} fue: {1}".format(i, oracion[i-1]))

        # Unir y mostrar sin espacio
        print ("La oración unida sin espacio es:")
        print ("".join(oracion))
        break

    elif metodo == '2':
        oracion_list = oracion.split()

        #Mostrar sin espacio
        for i in range(1,len(oracion_list)+1):
            print("La palabra {0} fue: {1}".format(i, oracion_list[i-1]))

        # Unir y mostrar sin espacio
        print (re.sub(' ', '', oracion))
        break
    else:
        print("Escogé un modo valido, mardito") 

print("\nPresione Enter para salir...")
input()
