try:
    # Pedimo la cantidad total por teclado
    total=float(input("Por favor, inserta la cantidad total de la compra:"))
except ValueError:
    print("ERROR: Debe de ser una cantidad numérica...")
else:
    dia=input("Es marte o jueves (Sí o No)").upper()
    
    if(dia=="SI" or dia=="SÍ"):
        descuento=total*0.15
        total=total - descuento
        print("\nEl descuento es: ",descuento)
        print("El total a pagar es: ",total)
    elif (dia=="NO"):
        print("\nNo tienes descuento, el total a pagar es: ",total)
    else:
        print("\nError:Opción no Valida")