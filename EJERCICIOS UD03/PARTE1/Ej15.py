# Leemos dos números por teclado
num1=input("Introducir un primer número: ")
num2=input("Introducir un segundo número: ")

if(num1!=num2):
    if(num1>num2):
        print(f"El número {num1} es el mayor de los dos.")
        print(f"El número {num2} es el menor de los dos.")
    else:
        print(f"El número {num2} es el mayor de los dos.")
        print(f"El número {num1} es el menor de los dos.")
else:
    print(f"Los dos número son iguales {num1}")