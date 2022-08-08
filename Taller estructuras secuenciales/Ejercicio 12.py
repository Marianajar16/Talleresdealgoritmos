#entrada
matematicas_uno=float(input("Ingrese nota del examen matematicas: "))
matematicas_dos=float(input("Ingrese nota de tarea 1 math: "))
matematicas_tres=float(input("Ingrese nota de tarea 2 math: "))
matematicas_cuatro=float(input("ingrese nota de tarea 3 math: "))
fisica_uno=float(input("Ingrese nota del examen fisica: "))
fisica_dos=float(input("Ingrese nota de tarea 1 fis: "))
fisica_tres=float(input("Ingrese nota de tarea 2 fis: "))
quimica_uno=float(input("Ingrese nota del examen quimica: "))
quimica_dos=float(input("Ingrese nota de tarea 1 quim: "))
quimica_tres=float(input("Ingrese nota de tarea 2 quim: "))
quimica_cuatro=float(input("ingrese nota de tarea 3 quim: "))
#caja negra
matematicas_final=((matematicas_uno*0.90)+(((matematicas_dos+matematicas_tres+matematicas_cuatro)/3)*0.10))
fisica_final=((fisica_uno*0.80)+(((fisica_dos+fisica_tres)/2)*0.20))
quimica_final=((quimica_uno*0.85)+(((quimica_dos+quimica_tres+quimica_cuatro)/3)*0.15))
promedio_total=(matematicas_final+fisica_final+quimica_final)/3
#salidas
print("La nota final de matematicas es:"+str(matematicas_final))
print("La nota final de quimica es:"+str(quimica_final))
print("la nota final de fisica es:"+str(fisica_final))
print("El promedio general de las tres notas es:"+str(promedio_total))