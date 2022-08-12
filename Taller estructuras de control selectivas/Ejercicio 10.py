#entradas
s=int(input("Digite su salario:") ) 
c=int(input("Digite su categoria del 1 al 5: ")) 
#caja negra
if (c==1):
  a=s*.10
if (c==2): 
  a=s*.15 
if (c==3):
  a=s*.20
if (c==4): 
 a=s*.40
 if (c==5): 
  a=s*.60 
sn=s+a
#salidas 
print("El aumento sera de: "+str(a))
print("Valor del sueldo nuevo: " +str(sn))