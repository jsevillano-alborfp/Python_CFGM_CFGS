"""
Crea una aplicación que dibuje una escalera de asteriscos. Nosotros le pasamos la altura de la escalera por teclado. Este es un ejemplo si insertaras un 5 de altura:
*
**
***
****
*****
"""

try:
    # Pedimos la altura de la escalera
    altura=int(input("Intruce la altura de la escalera: "))
    if altura<=0:
        raise ValueError
except ValueError:
    print("ERROR: Eres muy tonto, solamente son validos números enteros")
else:
# -----------------------------------------
    print("\nForma nº1")
    for i in range(1,altura+1):
        for j in range(1,i+1):
            print("*",end="")
        print()
# -----------------------------------------
    print("\nForma nº2")
    asterisco="*"
    for i in range(1,altura+1):
        print (asterisco)
        asterisco=asterisco+"*"
# -----------------------------------------
    print("\nForma nº3")
    for i in range(1,altura+1):
        print("*"*i)