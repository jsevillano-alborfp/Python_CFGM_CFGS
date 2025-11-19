# Suma independiente de los pares y de los impares de los números comprendidos entre 100 y 200.add()
pares=impares=0

for i in range(100,201):
    if(i%2==0):
        pares=pares+i
    else:
        impares=impares+i

# Mostramos el resultado
print(f"La suma de los pares es: {pares}\nLa suma de los impares es: {impares}")