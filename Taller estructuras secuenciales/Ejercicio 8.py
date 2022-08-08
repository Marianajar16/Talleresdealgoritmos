
import math
#entrada
a=float(input("Ingrese lado a: "))#float
b=float(input("Ingrese lado b: "))#float
c=float(input("Ingrese lado c: "))#float
#caja negra
s=(a+b+c)/2 #float
area=math.sqrt(s*(s-a)*(s-b)*(s-c))#float
#salidas
print("Area:"+str(area))