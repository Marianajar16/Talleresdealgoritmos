#entradas
can_bolivar=int(input("Cantidad de préstamo de Bolívares: "))
interes=int(input("Cantidad de intereses en 4 años: "))
#caja negra
ppr=(interes*100)/(can_bolivar*4)
porcentaje=ppr/4
#salida
print("El porcentaje anual cobrado por el prestamo es de:",porcentaje)