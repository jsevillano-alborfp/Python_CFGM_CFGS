# Pedimos el nombre del trabajador
nombreTrabajador=input("Insertar el nombre del trabajador:")
# Pedimos el número de horas trabajadas
numHoras=float(input("Insertar el numero de horas trabajadas para calcular el salario neto:"))

# Calculamos lo que tenemos que pagar por el número de horas trabajadas
tarifaNormal=35

# Salario Bruto
salarioBruto=0

if(numHoras<=35):
    salarioBruto=salarioBruto+(numHoras*tarifaNormal)
elif (numHoras>35):
    salarioBruto=salarioBruto+(35*tarifaNormal)
    numHoras=numHoras-35
    salarioBruto=salarioBruto+(numHoras*(1.5*tarifaNormal))

# Vamos a calcular las tasas de impuestos
auxSalarioBruto=salarioBruto
salarioNeto=0

if (auxSalarioBruto<=500):
    salarioNeto=salarioNeto+auxSalarioBruto
elif (auxSalarioBruto>500):
    salarioNeto=salarioNeto+500
    auxSalarioBruto=auxSalarioBruto-500
    if(auxSalarioBruto<=400):
        salarioNeto=salarioNeto+(auxSalarioBruto-(auxSalarioBruto*0.25))
    elif(auxSalarioBruto>400):
        salarioNeto=salarioNeto+(400-(400*0.25))
        auxSalarioBruto=auxSalarioBruto-400
        salarioNeto=salarioNeto+(auxSalarioBruto-(auxSalarioBruto*0.45))

print(f"El empleado con nombre {nombreTrabajador}, tiene de salario bruto {salarioBruto:.2f}, las tasas son {salarioBruto-salarioNeto:.2f} y de salario neto {salarioNeto:.2f}")     