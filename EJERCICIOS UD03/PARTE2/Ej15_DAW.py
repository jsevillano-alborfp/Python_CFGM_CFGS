"""
Crea una aplicación que dibuje una pirámide de asteriscos. Nosotros le pasamos la altura de la pirámide por teclado. Este es un ejemplo, si introducimos 5 de altura:
"""

try:
    # Pedimos la altura de la escalera
    altura=int(input("Intruce la altura de la pirámide: "))
    if altura<=0:
        raise ValueError
except ValueError:
    print("ERROR: Eres muy tonto, solamente son validos números enteros")
else:
# -----------------------------------------
    print("\nForma nº1:")
    for i in range(1,altura+1):
        # Vamos a construir los espacios
        for j in range(0,i-1):
            print(" ",end="")
        # Vamos a consturir los asteriscos
        for k in range(0,(2*altura+1)-(i*2)):
            print("*",end="")
        print("")
# -----------------------------------------
    print("\nForma nº2:")
    for i in range(1,altura+1):
        # Vamos a construir los espacios
        print(" "*(i-1),end="")
        # Vamos a consturir los asteriscos
        print("*"*((2*altura+1)-(i*2)))
# -----------------------------------------
    print("\nForma nº3:")
    for i in range(1,altura+1):
        # Vamos a construir los espacios
        print(" "*(i-1),"*"*((2*altura+1)-(i*2)))