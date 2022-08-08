#entradas
precio_producto=int(input("Ingrese el precio final de su producto: "))
precio_venta=int(input("Ingrese el precio de venta al publico del producto: "))
#caja negra
d=(precio_venta-precio_producto)
des=(d/precio_venta)*100
#salidas
print("El porcentaje de descuento es:",des)