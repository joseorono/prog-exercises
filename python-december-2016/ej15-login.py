"""
Crear un diccionario donde cada llave (key) sea un nombre de usuario y cada valor una contraseña, luego hacer un menu donde el usuario pueda:
Crearse una cuenta (se debe arrojar error si intenta crear una cuenta con un nombre de usuario ya existente)
Eliminar su cuenta (se le debe pedir la contraseña y preguntarle “Está seguro que desea eliminar su cuenta?”)
Iniciar sesión en una ya existente (se debe mostrar un error si el usuario intenta ingresar a una cuenta que no existe o si introduce 
una contraseña incorrecta).
Ver una lista de las cuentas existentes
Salir del programa (usar exit() )

Las contraseñas nuevas deben tener las siguientes características para ser consideradas válidas:
Deben tener un largo de al menos 5 caracteres
Deben tener al menos un número
No deben tener puntos, comas ni guiones (-), pero los pisos (_) son perfectamente aceptables.
El menú debe volver a aparecer luego de usar alguna de las funciones (usar ciclo while infinito).
  
   
"""


# =============================================================
#               FUNCIONES
# =============================================================

def mostrar_usuarios():
    for i in cuentas.values():
        print(i)

def iniciar_sesion(usuario,contrasena):
    if usuario in cuentas.keys():
        # Verificar contraseña
        if cuentas[usuario] == contrasena:
            print("Inicio de sesión realizado correctamente.")
            return True
        else:
            print("Contraseña incorrecta.")
            return False
    else:
        print("No existe un usuario con ese username.")
        return False


def eliminar_cuenta(usuario,contrasena):
    if usuario in cuentas.keys():
        # verificar contrasena
        if cuentas[usuario] == contrasena:
            while True:
                confirmar = str(input("Desea eliminar la cuenta {}? (Y/N)".format(usuario)))
                if confirmar == 'y':
                    del cuentas[usuario]
                    print("La cuenta fue eliminada correctamente.")
                    break
                elif confirmar.lower == 'n':
                    print("La cuenta no fue eliminada.")
                    break
                else:
                    print("ERROR: Opción invalida.")

    else:
        print("No existe un usuario con ese username.")


# =============================================================
#               VARIABLES
# =============================================================


global cuentas
sesion = False

cuentas = {
        "carlangas99": "elcarlito123",
        "Vitico92": "soyelnomberwanpapa1",
        "ElMalPortado": "papipuro69",
        "ElJoseph": "JanJozefo96",
        "PatriciaCandanga": "123VIVETUVIDA",
        }

# =============================================================
#               MAIN
# =============================================================


while True:
    # Si el usuario inicio sesión, darle la bienvenida
    if sesion ==  True:
        print("Bienvenido, {}!".format(cuenta_activa))

    print("\n==========OPCIONES=========")
    print("1. Iniciar sesión")
    print("2. Crear una cuenta nueva")
    print("3. Eliminar una cuenta")
    print("4. Ver lista de usuarios")
    print("5. Salir")

    opcion = input("\nQué opción desea utilizar? ")

    if opcion == '1':
        usuario = input("Usuario: ")
        contrasena = input("Contraseña: ")
        sesion = iniciar_sesion(usuario,contrasena)
        cuenta_activa = usuario 
    elif opcion == '3':
        usuario = input("Usuario: ")
        contrasena = input("Contraseña: ")
        eliminar_cuenta(usuario,contrasena)
    elif opcion == '4':
        mostrar_usuarios()
    elif opcion == '5':
        exit()


