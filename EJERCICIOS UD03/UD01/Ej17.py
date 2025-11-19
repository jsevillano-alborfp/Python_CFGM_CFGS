# Leemos dos números por teclado
num1=int(input("Insertar un número: "))
num2=int(input("Intregar un número: "))

# Mostramos los número en orden ascendente
if (num1>num2):
    print(f"{num1}>{num2}")
else:
    print(f"{num2}>{num1}")