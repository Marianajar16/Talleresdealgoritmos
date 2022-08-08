import math
#entradas
parcial_uno=float(input("Digite nota del parcial uno: "))
parcial_dos=float(input("Digite nota del parcial dos: "))
parcial_tres=float(input("Digire nota del parcial tres: "))
examen=float(input("Digite nota del examen: "))
trabajo=float(input("Digite nota del trabajo final: "))
#caja negra 
calificacion_final=((((parcial_uno+parcial_dos+parcial_tres)/3)*0.55)+(examen*0.3)+(trabajo*0.15))
#salida
print("La nota final es:"+str(calificacion_final))