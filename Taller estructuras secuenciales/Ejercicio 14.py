#entradas
l_uno=int(input("Ingrese la lectura anterior de kilovatios: "))
l_dos=int(input("Ingrese la lectura actual de kilovatios: "))
l_tres=int(input("Ingrese el costo por kilovatio: "))
#caja negra
monto=abs(l_dos-l_uno)*l_tres
#salida
print("El monto total a pagar en un mes de luz electrica es:",monto)