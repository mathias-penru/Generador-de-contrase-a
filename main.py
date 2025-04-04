# Generador-de-contrase-a
Generador: Contraseña

 import random 

Variable =  "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

XZ1 = int(input("De cuantos caracteres quiere su contraseña"))
Password = ""

for i in range(XZ1):
    Password += random.choice(Variable)

print(Password)    
