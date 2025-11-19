print("Los números pares comprendidos entre el 1 y 200 son:")

# Mostramos por pantalla los números pares del 1 al 200 de dos en dos
for i in range(1,201):
    if(i%2!=0):
        print(f"{i} ",end='')