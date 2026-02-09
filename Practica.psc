Algoritmo Practica
	Definir cajero,cuentaDeAhorro,numeroDeCuenta, cantidadSaliente, saldo, preguntar Como Entero
	CuentaDeAhorro = 1000
	numeroDeCuenta = 12345
	Escribir " Bienvenido"
	Escribir "Actividad que desea realizar"
	Escribir " 1 para consultar"
	Escribir " 2 para para extraer dinero de la cuenta de ahorro"
	
	Escribir "Escriba el numero de cuenta a operar"
	Leer preguntar
	
	si preguntar == 1
		Escribir "Escriba el numero de cuenta a operar"
		Leer preguntar
		
		si preguntar == numeroDeCuenta
			Escribir " su saldo es de " , cuentaDeAhorro
		FinSi
		Finsi
		
		si  preguntar == 2
			Escribir  " Escriba el nunero de cuenta a operar"
			Leer preguntar // es valor den numero de cuentas
			si preguntar == numeroDeCuenta
				Escribir  " Escriba el monto a extraer"
				Leer preguntar // es la cantidad a extraer
				// < =
				si preguntar <= cuentaDeAhorro
					Saldo = cuentaDeAhorro - preguntar
					Escribir  "Procesando"
					Escribir  "Su saldo actual es de " , Saldo
				FinSi
			FinSi
		FinSi
FinAlgoritmo
