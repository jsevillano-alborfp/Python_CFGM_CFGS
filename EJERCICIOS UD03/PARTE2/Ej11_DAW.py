# Crear escalera pidiendo por teclado la altura

# Pedir altura:
try:
    altura=int(input("Insertar la altura de la escalera: "))
except ValueError:
    print("ERROR: Eres tonto ...")
else:
# -----------------------------------------------------------
    print("Forma 1:")
    cadena="*"
    for i in range(1,altura+1):
        print(cadena)
        cadena=cadena+"*"
# -----------------------------------------------------------
    print("\nForma 2:")
    for i in range(1,altura+1):
        for j in range(1,i+1):
            print("*",end="")
        print()
# -----------------------------------------------------------
    print("\nForma 3:")
    for i in range(1,altura+1):
        print("*"*i)