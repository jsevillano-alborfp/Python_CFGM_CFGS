# Definimos las variables necesarias para la ejecución
num=1
pos=0
neg=0

while(num!=0):
    num=int(input("Insertar un número positivo o negativo (Pulsar 0 para terminar la ejecución):"))
    
    if(num!=0):
        if(num>0):
            pos+=1
        else:
            neg+=1

if(neg>0):
    print("Se ha insertado números negativos...")

print(f"La cantidad de positivos son: {pos} \nLa cantidad de negativos son: {neg}")