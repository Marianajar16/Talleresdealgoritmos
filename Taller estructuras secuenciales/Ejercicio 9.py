#entradas
horas_trabajadas=float(input("Ingrese numero de horas trabajadas: "))
precio_hora=int(input("Digite el precio de la hora: "))
#caja negra
sueldo_base=(horas_trabajadas*precio_hora)
salario_neto=(sueldo_base)-(sueldo_base*0.20)
#salida
print("El salario neto del trabajador es: ",salario_neto)