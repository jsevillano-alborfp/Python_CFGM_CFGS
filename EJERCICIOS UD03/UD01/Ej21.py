# Variable contador para incrementar los 100 números que nos insertan por teclado
cont=0
# Variable bandera para marcar si nos han insertado un número nulo
bandera=0

# Leemos 100 números no nulo por teclado
while cont<100:
    num=int(input("Insertar un número: "))
    # Si es distinto de cero incrementamos la variable en uno
    if num!=0:
        cont+=1
        # Si insertan un número negativo ponemos la variable bandera a 1
        if num<0:
            bandera=1

# Comprobamos si tenemos la bandera a 1 para mostrar el mensaje si nos han insertado número negativo
if bandera==1:
    print("Han insertado algún número negativo.")
else:
    print("No han insertado ningún número negativo.")