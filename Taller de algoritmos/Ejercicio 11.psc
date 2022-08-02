Algoritmo ejercicio_cuatro
	// entrada
	Escribir "DIGITE calificacion_parcial_uno: "
	Leer calificacion_parcial_uno
	Escribir "DIGITE calificacion_parcial_dos: "
	Leer calificacion_parcial_dos
	Escribir "DIGITE calificacion_parcial_tres: "
	Leer calificacion_parcial_tres
	Escribir "DIGITE calificacion_examen: "
	Leer calificacion_examen
	Escribir "DIGITE calificacion_trabajo: "
	Leer calificacion_trabajo
	// caja negra
	calificacion_parcial<- ((calificacion_parcial_uno+calificacion_parcial_dos+calificacion_parcial_tres)/3)*0.55
	calificacion_examen<- calificacion_examen*0.3
	calificacion_trabajo<- calificacion_trabajo*0.15
	calificacion_final<- calificacion_parcial+calificacion_examen+calificacion_trabajo
	Escribir calificacion_parcial
	Escribir calificacion_examen
	Escribir calificacion_trabajo
	Escribir calificacion_final
FinAlgoritmo
