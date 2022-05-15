import sqlite3

miConexion = sqlite3.connect("PrimeraBase")
miCursor = miConexion.cursor()

miCursor.execute("SELECT * FROM PRODUCTOS")

variosProductos = miCursor.fetchall()

for producto in variosProductos:
	print("Nombre artículo: ", producto[0], " - Sección: ", producto[2])

miConexion.commit()

miConexion.close()

