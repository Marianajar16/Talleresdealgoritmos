Algoritmo Velocidades
	//entradas
	Escribir "Digite la velocidad de primer coche (km/h)"
	Leer v1
	Escribir "Digite la velocidad del segundo coche (km/h)"
	Leer v2
	Escribir "Digite la distancia (km)"
	Leer d
	//caja negra
	t1<-abs(d/(v1-v2))
	tt<-t1*60
	//salida
	Escribir "El tiempo en el que alcanzara el coche más lento al de más velocidad en minutos es de " tt
FinAlgoritmo
