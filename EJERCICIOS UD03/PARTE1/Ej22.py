"""
Escriba un programa que recibe como datos de entrada una hora expresada en horas, minutos y segundos que nos calcula y escribe la hora, minutos y segundos que serán, transcurrido un segundo.
"""

class ErrorProvocado(Exception):
    """_summary_
    *Creamos una clase para controlar el día, mes y año
    
    Args:
        Exception (_type_): _description_
    """
    def __init__(self, valor):
        self.valor = valor
        super().__init__(f"Se produjo un error: La/El {valor} no es válido.")

while True:
    try:
        #Pedimos dia, mes y año
        segundo=int(input("Introducir los segundos (del 0 al 59): "))
        if(segundo<0 or segundo>59):
            raise ErrorProvocado("Segundos")
        minutos=int(input("Introducir los minutos (del 0 al 59):"))
        if(minutos<0 or minutos>59):
            raise ErrorProvocado("Minutos")
        hora=int(input("Introducir la hora (del 0 al 23):"))
        if(hora<=0 or hora>23):
            raise ErrorProvocado("Hora")
        
        print(f"La hora es: {hora}:{minutos}:{segundo}.")
        
        if(segundo+2>59):
            segundo=(segundo+2)-60
            minutos+=1
            if(minutos>59):
                minutos=minutos-60
                hora+=1
                if(hora>23):
                    hora=hora-24
        
        print(f"La hora después de dos segundo es: {hora}:{minutos}:{segundo}.")
    except ErrorProvocado as e:
        print(e)
