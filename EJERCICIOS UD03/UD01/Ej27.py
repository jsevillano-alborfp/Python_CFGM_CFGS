# Leer una secuencia de notas (del 0 al 10) y cuando pulse -1 terminamos la ejeucicón y mostramos el mensaje si se ha introducido alguna nota con valor igual a 10
nota=0
bandera=0

while nota!=-1:
    nota= int(input("Insertar la nota que has obtenido (-1 para salir):"))
    if nota<0 or nota>10:
        print("ERROR: Nota no válida.")
    if(nota==10):
        bandera=1

if bandera==1:
    print("Se ha introducido alguna nota con valor igual a 10")
else:
    print("No se ha insertando ninguna nota con valor igual a 10")