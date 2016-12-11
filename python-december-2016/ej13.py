def c_numeros_str(txt):
    """
    Leee una cadena y verifica cuantos de sus caracteres son digitos.
    Regresa la cantidad como un numero entero
    """
    cont = 0
    numeros=['1','2','3','4','5','6','7','8','9','0']
    for i in range(len(txt)):
        if txt[i] in numeros:
            cont+=1
    return cont

def leernum_intpos(mensaje):
    """
    lee un numero entero positivo
    """
    while True:
        num = str(input(mensaje))
            
        if c_numeros_str(num) == len(num):
            return num
        else:
            print("Error: Debe ingresarse un numero entero positivo")

num1 = leernum_intpos("Ingrese el primer numero entero positivo: ")
num2 = leernum_intpos("Ingrese el segundo numero entero positivo: ")

# Intercambiar el ultimo numero de num1 por el primero de num2

num1, num2 = (num1[:len(num1)-1] + num2[0]), (num1[len(num1)-1] + num2[1:])

# mostrarlos 
print(num1)
print (num2)
