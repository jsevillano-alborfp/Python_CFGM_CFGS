import sys

# Pedimo por teclado el valor total de la compra
v_compra=float(input("Insertar el Valor Total de la Compra: "))

while(True):
    print("\n**** Menú del Programa ****")
    print("1.- Pargo al Contado (Descuento 5%).")
    print("2.- Pago con Tarjeta (Recargo 3%).")
    print("3.- Cancelar el Pago")
    opcion=int(input("Insertar opción: "))
    
    match opcion:
        case 1:
            precio_final=v_compra-(v_compra*0.05)
            print(f"\nEl precio final: {precio_final}")
            sys.exit()
        case 2:
            precio_final=v_compra+(v_compra*0.03)
            print(f"\nEl precio final: {precio_final}")
            sys.exit()
        case 3:
            break
        case _:# Default
            print("\nEres muy tonto, la opción no es valida....")