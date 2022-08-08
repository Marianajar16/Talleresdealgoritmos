#entradas
dinero_base=int(input("Digite sueldo base: "))
venta_uno=int(input("Digite venta 1: "))
venta_dos=int(input("Digite venta 2: "))
venta_tres=int(input("Digite venta 3: "))
#caja negra 
comision=((venta_uno+venta_dos+venta_tres)*0.1)
sueldo_total=(dinero_base+comision)
#salida
print("El valor del sueldo total del mes es: ",sueldo_total)
print("El valor total de las comisiones es de: ",comision)