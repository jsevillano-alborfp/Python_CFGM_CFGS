import random

# Sacamos un número aleatorio entre 1 y 100
num=random.randint(1,100)

# Variables utilizadas para la ejecución del programa
acertado=False
lanzar=50
uno=0

while acertado!=True:
    # Mostramos el número pensado
    print("\nEl numero pensado es:",num)
    print("\n************ OPCIONES DE LA APLICACION ************")
    print("1-Mayor\n2-Menor\n3-Acertaste")
    print(f"El número pensado corresponde al valor: {lanzar:.0f}")
    opcion=int(input("Introducir opcion:"))
    
    match opcion:
        case 1:
            if(uno==0):
                lanzar=lanzar+int(lanzar/2)
                uno=1
            else:
                lanzar+=1
        case 2:
            if(uno==0):
                lanzar=lanzar/2
                uno=1
            else:
                lanzar-=1
        case 3:
            acertado=True
            print(f"\nAcertaste el número pensado que corresponde con:  {lanzar:.0f}")
        case _: 
            print("\nERROR: Opción no Valida.....\n")