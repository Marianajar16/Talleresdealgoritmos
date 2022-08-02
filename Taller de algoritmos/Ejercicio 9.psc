Algoritmo dinero_vendedor
	//entradas
	Escribir "Digite su sueldo base"
	Leer sueldo_base
	Escribir "Digite el valor de la venta 1"
	leer venta_1
	Escribir "Digite el valor de la venta 2"
	leer venta_2
	Escribir "Digite el valor de la venta 3"
	Leer venta_3
	//caja negra 
	comision_por_ventas<- (venta_1+venta_2+venta_3)*0.10
	sueldo_total<- sueldo_base+comision_por_ventas
	//salidas
	Escribir "El dinero recibido por comisiones totales es: " comision_por_ventas
	Escribir "El sueldo total del mes es: " sueldo_total
	
FinAlgoritmo
