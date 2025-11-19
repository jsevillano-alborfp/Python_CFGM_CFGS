# Pedimos por teclado el número n
n=int(input("Introducir un número: "))

# Mostramos todos los números desde 1 hasta n incluido
for i in range(1,n+1):
    print(f"{i} ",end='')