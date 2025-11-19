try:
    # Pedimos la altura de la escalera
    altura=int(input("Intruce la altura de la escalera: "))
    if altura<=0:
        raise ValueError
except ValueError:
    print("ERROR: Eres muy tonto, solamente son validos números enteros")
else:
# -----------------------------------------
    print("\nForma nº1")
    for i in range(1,altura+1):
        for j in range(1,i+1):
            print(j,end="")
        print()
# -----------------------------------------
    print("\nForma nº2")
    escalera="1"
    for i in range(2,altura+2):
        print(escalera)
        escalera=escalera+str(i)
# -----------------------------------------
    print("\nForma nº3")
    bandera=1
    while(bandera<=altura):
        for i in range(1,bandera+1):
            print(i,end="")    
        print()
        bandera+=1