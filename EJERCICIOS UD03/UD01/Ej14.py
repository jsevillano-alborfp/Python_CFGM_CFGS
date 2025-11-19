# Pedimos dos números por teclado
num1=int(input("Introducir el primer número: "))
num2=int(input("Introducir el segundo número: "))

print()

# Realizamos la operaciones de suma, resta, multiplicación y división
suma=num1+num2
resta=num1-num2
multiplicacion=num1*num2

# Controlamos la división por cero
if num1==0 or num2==0:
    division=0
else:
    division=num1/num2

# Mostramos el resultado por pantalla
print(f"El resultado de la suma es: {suma}")
print(f"El resultado de la restga es: {resta}")
print(f"El resultado de la multiplicacion es: {multiplicacion}")

# Controlamos la división por cero
if num1==0 or num2==0:
    print(f"El resultado de la division es: {division}")
else:
    print(f"El resultado de la division es: {division:.3}")
