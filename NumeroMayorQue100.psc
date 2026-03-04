Algoritmo NumeroMayorQue100
	Definir num Como Entero
	Definir promedio Como Real
	Definir ciclo Como Logico
	
	ciclo <- Verdadero
	Repetir
		Escribir " hola papi, porfa esriba un numero que sea mayor a 100"
		Leer num
		promedio <- num/2
		Si NO (num > 100) Y (ciclo = Verdadero) Entonces
			Escribir "El número ", num, " es menor o igual a 100. vuelve a intentar."
			Escribir "Dato curioso: La mitad de tu número es ", promedio " no es interesane este dato papi!!"
		Sino
			ciclo <- Falso 
			Escribir " sip papi el número ", num, " es mayor que 100."
		FinSi
			
			
	Hasta Que ciclo = Falso
	Escribir " Bye cidate"
	
FinAlgoritmo
