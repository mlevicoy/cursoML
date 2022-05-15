import sqlite3

miConexion = sqlite3.connect("GestionProductos")
miCursor = miConexion.cursor()

#miCursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION = 'confección'")
#productos = miCursor.fetchall()
#print(productos)

#miCursor.execute("UPDATE PRODUCTOS SET PRECIO = 35 WHERE NOMBRE_ARTICULO = 'pelota'")

miCursor.execute("DELETE FROM PRODUCTOS WHERE ID = 5")


miConexion.commit()
miConexion.close()
