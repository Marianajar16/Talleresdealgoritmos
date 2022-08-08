#entradas
can_naranjas=int(input("Digite cantidad de naranjas compradas: "))
precio=int(input("Digite el precio por una docena de naranjas: "))
venta=int(input("Digite el precio por el cual se vendieron las naranjas: "))
#caja negra
inv=(can_naranjas*precio)/12
stonks=(venta-inv)*100/inv
print("El porcentaje de ganancia en la inversion es:",stonks)