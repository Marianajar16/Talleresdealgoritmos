#Entradas
chelines=int(input("Ingrese la cantidad de chelines austriacos: "))
dracmas=int(input("Ingrese la cantidad de dracmas griegos: "))
pesetas=int(input("Ingrese la cantidad de pesetas: "))
#Caja negra
chelin_peseta=chelines*9568.71
dracma_franco=(dracmas*886.07)/20110
peseta_dolar=pesetas*0.00000816
peseta_liria=pesetas/92.89
#Salidas
print("El equivalente de chelines a pesetas es:",chelin_peseta) 
print("El equivalente de dracmas griegos a francos es:",dracma_franco) 
print("El equivalente de pesetas a dolares es:",peseta_dolar) 
print("El equivalente de pesetas a liras italianas es:",peseta_liria) 