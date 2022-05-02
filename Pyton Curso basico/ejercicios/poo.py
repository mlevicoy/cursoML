class Coche():
	def __init__(self):
		# Encapsulación de propiedades (variables)
		self.__largoChasis = 250
		self.__anchoChasis = 120
		self.__ruedas = 4
		self.__enmarcha = False

	def arrancar(self, arrancamos):
		self.__enmarcha = arrancamos
		if(self.__enmarcha):
			return "El coche esta en marcha"
		else:
			return "El coche esta detenido"

	def estado(self):
		print("El coche tiene ", self.__ruedas, " ruedas. Un ancho de ", self.__anchoChasis, " y un largo de ", self.__largoChasis)

# Instanciamos a la clase Coche
miCoche = Coche()

print(miCoche.arrancar(True))

miCoche.estado()

# Instanciamos de nuevo
miCoche2 = Coche()

print(miCoche2.arrancar(False))

miCoche2.ruedas = 2

miCoche2.estado()



