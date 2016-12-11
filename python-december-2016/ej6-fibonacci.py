#fibonacci con una lista

fib=[0,1]
limite = input("Hasta que elemento de la sucesion se desea calcular? ")

for i in range(2,limite):
    fib.append(fib[i-1]+fib[i-2])

print (fib)
