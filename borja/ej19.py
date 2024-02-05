# trabajar con SQLite
import sqlite3

# Crear una conexión
conexion = sqlite3.connect('ejemplo.db')

# Crear un cursor
cursor = conexion.cursor()

# Crear una tabla
cursor.execute("CREATE TABLE usuarios (nombre text, edad integer, email text)")

# Cerrar la conexión
conexion.close()
