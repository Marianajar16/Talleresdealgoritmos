#entradas
s=int(input("Digite salario: "))
vd1=int(input("Digite ventas totales del departamento 1: "))
vd2=int(input("Digite ventas totales del departamento 2: "))
vd3=int(input("Digite ventas totales del departamento 3: "))
#caja negra
ventotal=(vd1+vd2+vd3)
print("venta total: "+str(ventotal))
e33=(ventotal*33)/100
if(vd1>e33):
    vd1=s+s*.20
else:
    vd1=s
print("Los vendedores del departamento 1 recibiran: "+str(vd1))      
if(vd2>e33):
    vd2=s+s*.20
else:
    vd2=s   
print("Los vendedores del departamento 2 recibiran: "+str(vd2))    
if(vd3>e33):
    vd3=s+s*.20
else:
    vd3=s        
print("Los vendedores del departamento 3 recibiran: "+str(vd3))  