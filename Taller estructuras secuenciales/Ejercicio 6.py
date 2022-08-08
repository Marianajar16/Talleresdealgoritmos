#entrada
estudiantes=int(input("Numero total de estudiantes: "))
mujeres=int(input("Numero de mujeres en el grupo: "))
hombres=int(input("Numero de hombres en el grupo: "))
#caja megra
porcentaje_mujeres=((mujeres/estudiantes)*100)
porcentaje_hombres=((hombres/estudiantes)*100)
#salidas
print("El porcentaje de hombres en el grupo es: ",porcentaje_hombres)
print("El porcentaje de mujeres en el grupo es: ",porcentaje_mujeres)
