# Definimos dos variables para el nombre de usuario y contraseña
user="Juan"
pas="1234"

#Pedimos usuarios y contraseña por teclado
_user=input("Insertar el nombre de usuario: ")
_pas=input("Insertar la contraseña del usuario: ")

if(user!=_user):
    print("Usuario incorrecto....")
elif (pas==_pas):
    print("Sesión iniciada correctamente!!!!!!")
else:
    print("Contraseña es incorrecta.....")