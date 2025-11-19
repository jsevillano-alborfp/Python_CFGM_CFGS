def calcular_billetes(cantidad):
    """
    *Calcula el mínimo número de billetes necesarios para una cantidad dada.
    
    @Parámetros:
    @cantidad (int): Cantidad de euros, múltiplo de 5.
    
    !Retorna:
    !dict: Diccionario con billetes como claves y cantidad de cada billete como valores.
    """
    billetes = [500, 200, 100, 50, 20, 10, 5]  # Lista de billetes disponibles ordenados de mayor a menor
    resultado = {}  # Diccionario para guardar la cantidad de billetes de cada tipo
    for billete in billetes:
        count = cantidad // billete  # Número de billetes de esta denominación que caben en la cantidad
        if count > 0:
            resultado[billete] = count  # Guardar cantidad necesaria para este billete
            cantidad = cantidad % billete  # Actualizar la cantidad restante a distribuir
    return resultado

def main():
    """
    Función principal que solicita la cantidad al usuario, valida que sea múltiplo de 5, 
    calcula los billetes necesarios y muestra el resultado.
    """
    cantidad = int(input("Introduce una cantidad múltiplo de 5 €: "))  # Entrada del usuario
    if cantidad % 5 != 0:
        print("La cantidad debe ser múltiplo de 5 €.")  # Mensaje de error si no es múltiplo de 5
        return  # Termina el programa
    billetes_necesarios = calcular_billetes(cantidad)  # Calcula billetes mínimos necesarios
    print("Billetes necesarios:")
    for billete, cantidad_billetes in billetes_necesarios.items():
        print(f"{cantidad_billetes} billete(s) de {billete} €")  # Mostrar resultado

if __name__ == "__main__":
    main()
