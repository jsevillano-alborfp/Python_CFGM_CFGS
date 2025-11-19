# Variable contador para incrementar los 100 números que nos insertan por teclado
cont=0
# Variable para contar los positivos
pos=0
# Variable para contar los negativos
neg=0

# Leemos 100 números no nulo por teclado
while cont<100:
    num=int(input("Insertar un número: "))
    # Si es distinto de cero incrementamos la variable en uno
    if num!=0:
        cont+=1
        # Si insertan un número negativo ponemos la variable bandera a 1
        if num<0:
            pos+=1
        elif num>0:
            neg+=1

# Comprobamos si tenemos la bandera a 1 para mostrar el mensaje si nos han insertado número negativo
print(f"La cantidad de positivo es: {pos}")
print("La cantidad de positivos es: ",neg)