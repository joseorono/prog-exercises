import random
import string

# ================================================================
#   Funciones
# ================================================================


def generar_contrasena():
    """
    Genera una contrasena compuesta de numeros y letras minusculas
    """
    # Crea una lista vacia para la contraseña
    contrasena = []
    # Fija su largo y la cantidad de letras de numeros que contiene
    largo = random.randint(6,12)
    cant_numeros = random.randint(1,(largo // 2)+1)
    # Mostrar cuantos numeros tendra (solo para testing)
    # print(cant_numeros)
    #Inicializar la contraseña para que todos los espacios 
    contrasena = ["" for x in range(largo)]
    #Rellenar con letras aleatorias
    for i in range(largo):
        contrasena[i] = random.choice(string.ascii_lowercase)
    # Remplazar 3 de los caracteres por musica
    num_index = []
    while True:
        index = random.randint(0,largo-1)
        if str(index) not in num_index:
            contrasena[index]=str(random.randint(0,9))
            num_index.append(str(index))
        # Repetir hasta que haya la cantidad de numeros definida 
        if len(num_index) == cant_numeros:
            break
        
    # Retornar la contrasena generada
    contrasena = "".join(contrasena)
    return contrasena


def fuerza_bruta(var_contrasena):
    # Inicializar 'descifrada' como una string vacia
    descifrada = ""

    # Crear lista con todos los caracteres posibles
    # (numeros y letras minusculas)
    posibilidades = list(string.ascii_lowercase) + [str(i) for i in range(10)] 

    # Probar posibilidades hasta encontrar la correcta
    for i in range(len(var_contrasena)):
        for x in posibilidades:
            if x == var_contrasena[i]:
                descifrada += x 
                print("Carácter encontrado: {0}".format(x))
    # Retornar contrasena descrifrada
    return descifrada


# ================================================================
#   / Funciones
# ================================================================

contrasena = generar_contrasena()
print("La contraseña generada fue: {0}".format(contrasena))

resultado = fuerza_bruta(contrasena)
print(resultado)

if resultado == contrasena:
    print("Funciona!")
