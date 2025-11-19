# Calculamos la suma y el producto de los primer 10 números naturales
suma=0
multiplicacion=1

for i in range(1, 11):
    suma+=i
    multiplicacion*=i

print(f"El valor de la suma es: {suma} \nEl valor del producto es: {multiplicacion}")