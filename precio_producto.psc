Algoritmo precio_producto
	Definir saldo, precioProducto,pregunta Como Entero
	saldo = 100
	precioProducto= 20
	Escribir " Hola bienvenido a esta tienda virtual"
	Escribir " en este dia tenemos un descuento de auriculares"
	Escribir " quiere verlos? Porfa precione un numero segun la accion a realizar"
	Escribir " 1 verificar mi dinero"
	Escribir " 2 ir a ver el producto"
	
	Leer pregunta
	
	si pregunta ==1
		Escribir " su dinero actual es de ", saldo, " dolares"
		Escribir " quiere ir a ver el producto? precione 2 si quiere ir a ver el producto, 4 si no quiere ir a ver el producto"
		Leer pregunta
	Finsi
	
	
		si pregunta ==2
		Escribir " el precio del producto es de ", precioProducto, " dolares, desea pagar?"
		Escribir " precione 3 para comprar y 4 para no comprar"
		Leer pregunta
		Finsi
		si pregunta ==3
			Escribir " Felicidadades usted compro unos auriculares marca nokia chinos"
			Finsi
			si pregunta ==4
				Escribir " bueno gracias por visitar la tienda virtual"
		FinSi
	
FinAlgoritmo
