# intercambiar 2 variables

a = input("Ingrese un valor para el primer numero: ")
b = input("Ingrese un valor para el segundo numero: ")
a, b = b, a

print ("Luego del intercambio...\na={0}\nb={1}".format(a,b))
