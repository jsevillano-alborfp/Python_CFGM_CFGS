import sys

try:
    # Pedimos un número por teclado
    print("Insertar un número que sea positivo (mayor que cero):")
    num=int(input())
    
    # Cromprobamos si el número es negativo o cero
    if num<0:
        raise ValueError("El número no puede ser negativo ni cero.")
    else:
        # Si el número insertado es 0 mostramos el factorial de cero e interrumpimos la ejecución
        if num==0:
            print(f"El factorial de 0 es: 1")
            sys.exit
    # Variable para almacenar el factorial
    factorial=1
    
    # Realizamos el factorial del número
    for i in range(1,num+1):
         factorial = factorial*i
    
    #Mostramos el resultado:
    print(f"El factorial de {num} es: {factorial}")
except ValueError as e:
    print ("Error: ",e)