# Leemos el precio de un artículo
precioArticulo=float(input("Introducir el precio del artículo: "))

# Leemos el precio de venta de un artículo
precioVentaReal=float(input("Introducir el precio de venta del artículo: "))

# Calculamos el porcentaje de descuento
porcentaje=((precioVentaReal-precioArticulo)/precioVentaReal)*100

# Mostramos el procentaje de descuento
print(f"El porcentaje de descuento es: {porcentaje:.2f}%")