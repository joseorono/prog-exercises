# Hallar todas las ocurrencias de un elemento en una lista

def ocurrencias(iterable,elemento):
    """
    Crea una lista vacia, la llena con todos los indices donde encuentra 'elemento'
    en 'iterable' y la regresa
    """
    ocurrencias = []
    
    for i in range(0,len(iterable)):
        if iterable[i] == elemento:
            ocurrencias.append(i)
    
    return ocurrencias

lista_recetas = ["biscocho","sopa","paella","sopa","galleta"]

print("La lista de recetas es: \n{0}".format(lista_recetas))
buscar = input("Que receta desea buscar: ")
en_indices = ocurrencias(lista_recetas,buscar)

if len(en_indices) > 0:
    for i in range(len(en_indices)):
        print("El elemento {0} aparece en el indice {1} de la lista".format(buscar,en_indices[i]))
else:
    print("No se encontró el elemento en la lista.")
