# Pedimos un número por teclado
while True:
    try:
        numero=int(input("Insertar un número para calcular si es múltiplo de 10: "))
        break
    except ValueError:
        print("Error: Debes de insertar un número")

if(numero%10==0):
    print(f"El número {numero} SI es múltiplo de 10.")
else:
    print(f"El número {numero} MO es múltiplo de 10.")