
mayor = 0

while True:
    
    num = input("Ingrese un numero: ")
    
    # si num es mas alto que 'mayor', se le asigna num a mayor

    if num>0:
        if num>mayor:
            mayor=num
    else:
        print ("ERROR: Debe introducirse en valor mayor a 0")

    
    if num== -99:
        break

print ("El numero mas alto fue {0}".format(mayor))
