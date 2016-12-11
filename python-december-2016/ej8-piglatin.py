# Traductor de una palabra a Pig-Latin

# Esta funcion determina si un caracter es una vocal
def esvocal(char):
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        return True
    else:
        return False

# Leer una palabra
while True:
    palabra= input("Ingrese una palabra: ")
    if palabra.isalpha() == True and len(palabra) > 1:
        break
    else:
        print ("Debe introducir una palabra, no un número ni un carácter, ni una oración")

# Traducir
if esvocal(palabra[0]) == True:
    palabra = palabra + "ay"
else:
    # Mover al final todas las consonantes que hayan antes de la primera vocal
    while esvocal(palabra[0]) == False:
        palabra = palabra[1:] + palabra[0]
    # Añadir "ay" al final
    palabra += "ay"

print("Su palabra en Pig Latin:\n{0}".format(palabra))
