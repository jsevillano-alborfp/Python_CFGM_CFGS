# Variable num con valor igual que -1
num=-1

while(num<=0 or num>99999):
    # Leemos un número por teclado
    num = int(input("Insertar un número: "))

# Mostramos el número de dígitos que tiene
num= str(num)

print(f"El número de dígitos que tiene el número {num} es: {len(num)}")