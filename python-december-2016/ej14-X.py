def c_numeros_str(txt):
    """
    Leee una cadena y verifica cuantos de sus caracteres son digitos.
    Regresa la cantidad como un numero entero
    """
    cont = 0
    numeros=['1','2','3','4','5','6','7','8','9','0']
    for i in range(len(txt)):
        if txt[i] in numeros:
            cont+=1
    return cont

# Leer el numero de caracteres que tendra cada linea de la X
while True:
    caracteres = str(input("Ingrese el numero impar: "))
    if c_numeros_str(caracteres) == len(caracteres):
        caracteres = int(caracteres)

        if caracteres % 2 != 0:
            break
        else:
            print("El numero debe ser impar:")
    else:
        print("Debe ingresar un numero. No una palabra, o una frase. Un numero entero.")

# dibujar la X

espacios_centro = caracteres // 2

espacios_antes = 0
espacios_despues = caracteres - 2

for i in range(espacios_centro):
    # Espacios antes de X
    if espacios_antes > 0:
        for i in range(espacios_antes):
            print(" ", end="")

    print ("X", end="")
    for o in range(espacios_despues):
        print(" ", end="")

    if espacios_despues > 0:
        print("X")

     # Trabajar con contadores
    espacios_despues-=2
    espacios_antes+=1   

# Mostrar X central. Primero los espacios y luego la X
for i in range(espacios_centro):
    print(" ", end="")

print("X")

    # Las X que vienen luego del dentro, hasta que espacios
# Inicializo las variables de nuevo
espacios_antes = espacios_centro - 1
espacios_despues = 12
for i in range(espacios_centro):
    # Mostrar espacios de antes de la X
    for o in range(espacios_antes):
        print(" ",end="")
    # Mostrar X
    print("X",end="")
    #Mostrar espacios
    for o in range(espacios_despues):
        print(" ", end="")
    # Mostrar X con salto de linea normal
    print("X")

    # Operar contadores
    espacios_antes-=1
    espacios_despues+=2
