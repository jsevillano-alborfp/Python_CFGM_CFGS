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
        for j in range(i,altura):
            print(" ",end="")
        for k in range(1,2*i):
            print("*",end="")
        print("")