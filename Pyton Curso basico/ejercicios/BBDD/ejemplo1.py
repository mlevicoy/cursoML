import sqlite3

# Paso 1: Abrir conexion y crear DB
miConexion = sqlite3.connect("PrimeraBase")

# Paso 2: Crear puntero
miCursor = miConexion.cursor()

# Paso 3: Ejecutar consulta
miCursor.execute("CREATE TABLE IF NOT EXISTS PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")

miCursor.execute("INSERT INTO PRODUCTOS VALUES ('ALMOHADA', 10, 'ROPA DE CAMA')")

miConexion.commit()

# Paso 6: Cerrar conexión
miConexion.close()



