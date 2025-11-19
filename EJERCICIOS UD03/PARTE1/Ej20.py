# Leemos la calificación
calificacion=-1
while (calificacion<0 or calificacion>10):
    calificacion=int(input("Insertar la calificación:"))

# Mostramos la calificación obtenida
print("\n*** LA CALIFICACIÓN OBTENIDA ES: ****")

match calificacion:
    case 0|1|2: print("Muy Deficiente")
    case 3|4: print("Insuficinete")
    case 5: print("Suficinete")
    case 6: print("Bien")
    case 7|8: print("Notable")
    case 9|10: print("Sobresaliente")
    case _: print("Opción no Valida...")

print("\n\n Otra forma de hacer el MATCH - CASE con Rangos de valores mediante un if dentro del CASE\n\n")

match calificacion:
    case calificacion if calificacion>=0 and calificacion<=2: print("Muy Deficiente")
    case calificacion if calificacion>=3 and calificacion<=4: print("Insuficinete")
    case 5: print("Suficinete")
    case 6: print("Bien")
    case calificacion if calificacion>=7 and calificacion<=8: print("Notable")
    case calificacion if calificacion>=9 and calificacion<=10: print("Sobresaliente")
    case _: print("Opción no Valida...")