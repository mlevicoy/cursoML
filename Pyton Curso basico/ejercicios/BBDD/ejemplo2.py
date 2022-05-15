import sqlite3

miConexion = sqlite3.connect("PrimeraBase")
miCursor = miConexion.cursor()

variosProductos = [
("Camiseta", 10, "Deporte"),
("Jarrón", 90, "Cerámica"),
("Camión", 20, "Juguetería")
]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)", variosProductos)
miConexion.commit()

miConexion.close()


