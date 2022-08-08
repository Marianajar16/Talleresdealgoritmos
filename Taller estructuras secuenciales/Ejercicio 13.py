#Entradas
n1=int(input("Ingrese la cantida de billetes de 50000: "))
n2=int(input("Ingrese la cantida de billetes de 20000: "))
n3=int(input("Ingrese la cantida de billetes de 10000: "))
n4=int(input("Ingrese la cantida de billetes de 5000: "))
n5=int(input("Ingrese la cantida de billetes de 2000: "))
n6=int(input("Ingrese la cantida de billetes de 1000: "))
n7=int(input("Ingrese la cantida de billetes de 500: "))
n8=int(input("Ingrese la cantida de billetes de 100: "))
#Caja negra
cantidad_uno=n1*50000
cantidad_dos=n2*20000
cantidad_tres=n3*10000
cantidad_cuatro=n4*5000
cantidad_cinco=n5*2000
cantidad_seis=n6*1000
cantidad_siete=n7*500
cantidad_ocho=n8*100
cantidad_total=(cantidad_uno+cantidad_dos+cantidad_tres+cantidad_cuatro+cantidad_cinco+cantidad_seis+cantidad_siete+cantidad_ocho)
#Salidas
print("El dinero total en el banco es:",cantidad_total)