import re

print("==========================")
print("    O P C I O N E S")
print("==========================")
print("1 - cambiar vocales por 0")
print("2 - Lista de palabras con vocales")
print("3 - Eliminar numeros y letras de una string")
print("4 - Mostrar contrasenas con numeros en ellas")
print("5 - Ver si termina en '?'")
print("6 - Palabras que comienzan en vocales y consonantes")
print("==========================")
opc = input("Opciones seleccionada: ")

if opc == '1':
    # Puedo hacerle split() pero no es necesario, yay
    oracion = input("Introduzca string: ")
    print(re.sub(pattern,"0",oracion))
    
elif opc == '2':
    oracion = input("Introduzca string: ")
    # Verificar si cada elemento de la lista tiene vocales o no
    oracion = re.findall(r'\w*[a|e|i|o|u]+\w*',oracion)
    # Mostrar la lista resultante
    print(oracion)
    
elif opc == '3':
    oracion = input("Introduzca string: ")
    oracion = re.sub(r'\w',"",oracion)
    print(oracion)

elif opc == '4':
    # El diccionario de contraseñas
    cuentas = {
        "carlangas99": "elcarlito123",
        "Vitico92": "soyelnomberwanpapa1",
        "ElMalPortado": "papipuro69",
        "ElJoseph": "JanJozefo",
        "PatriciaCandanga": "123VIVETUVIDA",
        "PastelitosPipo": "QUESABROSOSSON",
        } 
    for key, value in cuentas.items():
        if re.search(r'[0-9]+',value):
            print(key)

elif opc == '5':
    oracion = input("Introduzca string: ")
    # Ver si tiene un signo de interrogacion al final
    # Metodo 1:
    if oracion.endswith("?"):
        print("Es una pregunta")
    else:
        print("No es una pregunta")
    # Metodo 2:
    if re.search(r'\?$',oracion):
        print("Es una pregunta")
    else: 
        print("No es una pregunta")

elif opc == '6':
    # Funciona pero no detecta las letras solas como palabras
    #oracion = input("Introduzca string: ")
    oracion  = "Eh, Traeme el chimichurri y el aguacate, primo A".split()
    print(oracion)
    #crear listas vacias
    comienza_consonante = []
    comienza_vocal = []
    # Esto CASI funciona
    # comienza_vocal = re.findall(r'\b[aeiou]+[a-z]*',oracion[i],re.IGNORECASE)
    # comienza_consonante = re.match(r'\b[^aeiou]+[a-z]*',oracion[i],re.IGNORECASE)
    for i in range(len(oracion)):
        if re.match(r'^[aeiou|AEIOU]+[a-zA-Z]*',oracion[i],re.IGNORECASE):
            comienza_vocal.append(re.sub(r'[^\w]',"",oracion[i]))
        elif re.match(r'[^aeiou]+[\w]*', oracion[i],re.IGNORECASE):
            comienza_consonante.append(re.sub(r'[^\w]',"",oracion[i]))
    #mostrar resultado
    print(comienza_vocal)
    print(comienza_consonante)
elif opc == '7':
    texto = """Jessica tiene 15, Daniel tiene 27.
    Edward tiene 97, y su abuelo Oscar 102."""
    edades = re.findall(r'\d{1,3}', texto)
    nombres = re.findall(r'[A-Z]+[a-z]+', texto)
    #Mostrar nombres y edades
    for i in range(len(nombres)):
        print("{0}:{1}".format(nombres[i],edades[i]))
