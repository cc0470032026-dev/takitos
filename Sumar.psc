Algoritmo Sumar
	// Solicitar al usuario que ingrese dos números enteros
	// y mostrar la suma de ambos.
	Definir numx, numy, resultado Como Entero
	Escribir ' Vienvenido al juego de la suma!!!'
	Escribir ' para comenzar podrias decirme tu nombre?'
	Leer nombre
	Escribir 'oh mucho gusto ', nombre, ', para comenzar dime un numero'
	Leer numx
	Escribir ' bien!!!, ahora dime otro numero'
	Leer numy
	Si numx>0 Entonces
		resultado <- numx+numy
	FinSi
	Escribir ' Hora de la magia, el resultado de la suma es ', resultado, ' jajaja soy increible'
FinAlgoritmo
