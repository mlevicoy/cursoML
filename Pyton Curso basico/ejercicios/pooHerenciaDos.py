class Persona():
	def __init__(self, nombre, edad, lugar_residencia):
		self.nombre = nombre
		self.edad = edad
		self.lugar_residencia = lugar_residencia

	def descripcion(self):
		print("\nNombre: ", self.nombre, "\nEdad: ", self.edad, 
			"\nLugar de residencia: ", self.lugar_residencia)

class Empleado(Persona):
	def __init__(self, salario, antiguedad, nombre_empleado, 
		edad_empleado, residencia_empleado):
		super().__init__(nombre_empleado, edad_empleado, residencia_empleado)
		self.salario = salario
		self.antiguedad = antiguedad

	def descripcion(self):
		super().descripcion()
		print("Salario: ", self.salario, "\nAntigüedad: ", self.antiguedad, " años")


Manuel = Empleado(2500, 5, "Manuel", "43", "Chile")
Manuel.descripcion()

# Principio de sustitución
print(isinstance(Manuel, Empleado))	




