#entradas
precio=int(input("Ingrese el precio de la compra: "))
recargo=float(input("Ingrese el interes de la compra por cada cuota: "))
#caja negra
cn=precio/12
cr=(cn*recargo)/100+cn
ci=(cr-cn)*100/cn
#salidas
print("El cobro en porcentaje por los intereses del computador es:",ci)
print("La cuota a pagar en conjunto al recargo mensual es:",cr)