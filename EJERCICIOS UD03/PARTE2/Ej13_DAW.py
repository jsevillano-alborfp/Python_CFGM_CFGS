# Escalera de números pidiendo la altura

# Pedir altura:
try:
    altura=int(input("Insertar la altura de la escalera: "))
except ValueError:
    print("ERROR: Eres tonto ...")
else:
# -----------------------------------------------------------
    print("Forma 1:")
    for i in range(1, altura+1):
        for j in range(1, i+1):
            print(j,end="")
        print()
# -----------------------------------------------------------
    print("Forma 2:")
    base="1"
    for i in range(1, altura+1):
        print(base)
        
        base=base+str(i+1)
# -----------------------------------------------------------
    print("Forma 3:")
    base="1"
    for i in range(2, altura+2):
        print(base)
        base=base+str(i)
     