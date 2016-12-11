# hacer un fizzbuzz

hasta = int(input("Hasta que numero desea hacer el fizzbuzz? "))


for i in range(1,hasta+1):
    if i % 3 == 0 and i % 5 == 0:
        print ("fizzbuzz")
    elif i % 3 == 0:
        print ("fizz")
    elif i % 5 == 0:
        print ("buzz")
    else:
        print (i)
