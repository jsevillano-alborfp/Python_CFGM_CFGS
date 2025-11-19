"""
Escriba un programa que simule un cajero automático con un saldo inicial de 1000 dólares, con el siguiente menú de opciones:
Bienvenido a su Cajero Virtual
1. Ingresar dinero en cuenta
2. Retirar dinero de la cuenta
3. Salir.
"""

saldo_inicial=1000

while(True):
    print("***** MENU DEL PROGRAMA *****")
    print("Bienvenido a su Cajero Virtual\n1.-Ingresar dinero en su cuenta.\n2.-Retirar dinero en su cuenta.\n3.-Salir del cajero.")
    opcion=int(input())
    
    match(opcion):
        case 1:
            print("\nEL SALDO ES: ",saldo_inicial)
            dinero=int(input("Insertar el dinero que quieres ingresar: "))
            saldo_inicial+=dinero
        case 2:
            print("\nEL SALDO ES: ",saldo_inicial)
            dinero=int(input("Insertar el dinero que quieres retirar: "))
            saldo_inicial-=dinero
        case 3:
            print("\nEL SALDO ES: ",saldo_inicial)
            print("Saliendo del cajero...")
            break
        case _: print("Opción no permitida...")