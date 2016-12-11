num=input("Introzca un numero: ")
acumulador=0

if 200%num==0:
    while acumulador<200:
        acumulador+=num
        print (acumulador)

else:
    print("Es imposible contar hasta 200 con el numero que introdujo")
