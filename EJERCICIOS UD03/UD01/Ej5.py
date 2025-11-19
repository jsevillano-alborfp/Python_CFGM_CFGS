import math

# Entrada: longitud del radio
radio = float(input("Introduce la longitud del radio: "))

# Cálculo del diámetro (el doble del radio)
diametro = 2 * radio

# Longitud de la circunferencia = pi * diámetro
longitud_circunferencia = math.pi * diametro

# Área del círculo = pi * radio^2
area_circulo = math.pi * radio**2

# Volumen de la esfera = (4/3) * pi * radio^3
volumen_esfera = (4/3) * math.pi * radio**3

# Mostrar resultados
print(f"Longitud de la circunferencia: {longitud_circunferencia:.2f}")
print(f"Área del círculo: {area_circulo:.2f}")
print(f"Volumen de la esfera: {volumen_esfera:.2f}")