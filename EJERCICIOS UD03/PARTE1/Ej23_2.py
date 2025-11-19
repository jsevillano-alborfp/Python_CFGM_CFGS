# Pedimo por teclado el valor total de la compra
v_compra=float(input("Insertar el Valor Total de la Compra: "))

bandera=True

while(bandera):
    print("\n**** Menú del Programa ****")
    print("1.- Pargo al Contado (Descuento 5%).")
    print("2.- Pago con Tarjeta (Recargo 3%).")
    print("3.- Cancelar el Pago")
    try:
        opcion=int(input("Insertar opción: "))
    except ValueError:
        print("Error: Solamente son Validos los Números....")
    else:
        if opcion==1:
            precio_final=v_compra-(v_compra*0.05)
            print(f"\nEl precio final: {precio_final}")
            bandera=False
        elif opcion==2:
            precio_final=v_compra+(v_compra*0.03)
            print(f"\nEl precio final: {precio_final}")
            bandera=False
        elif opcion==3:
            bandera=False
        else:# Default
                print("\nEres muy tonto, la opción no es valida....")