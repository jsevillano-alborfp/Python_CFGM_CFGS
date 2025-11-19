"""
Crea una aplicación que dibuje una escalera de asteriscos. Nosotros le pasamos la altura de la escalera por teclado. Este es un ejemplo si insertaras un 5 de altura:
"""
try:
    num=int(input("Insertar el tamaño de la escalera: "))
except ValueError:
    print("ERROR: Valor no valido.")
else:
    for i in range(1,num+1):
        for j in range(1,i+1):
           print("*",end="")
        print()
    print()
    variable="*"
    for i in range(1,num+1):
        if(i==1):
           print(variable)
        else:
            variable=variable+"*"
            print(variable)
"""
1 *
2 **
3 ***
"""