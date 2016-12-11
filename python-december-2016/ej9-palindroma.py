palabra = input("Elija una palabra y se verificara si es palindroma: ")
palabra_inv = palabra[::-1]

if palabra == palabra_inv:
    print ("Es palindroma")
else:
    print ("No es palindroma")
