# Clase padre
class Vehiculos():
	def __init__(self, marca, modelo):
		self.marca = marca
		self.modelo = modelo
		self.enmarcha = False
		self.acelera = False
		self.frena = False

	def arrancar(self):
		self.enmarcha = True

	def acelerar(self):
		self.acelerar = True

	def frenar(self):
		self.frena = True

	def estado(self):
		print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ", 
			self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena)

# Clase Furgoneta hereda de clase Vehículo
class Furgoneta(Vehiculos):
	def carga(self, cargar):
		self.cargado = cargar
		if self.cargado:
			return "La furgoneta está cargada"
		else:
			return "La furgoneta no está cargada"

# Clase Moto hereda de clase Vehículo
class Moto(Vehiculos):
	hcaballito = ""
	def caballito(self):
		self.hcaballito = "Voy haciendo el caballito"

	def estado(self):	
		print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ", 
			self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena,
			"\nCaballito: ", self.hcaballito)	

class VElectricos():
	def __init__(self):
		self.autonomia = 100
 
	def cargaEnergia(self):
 		self.cargando = True

# Instanciamos la clase Moto, y como hereda de 
# Vehículo se puede usar el constructor de esta.
miMoto = Moto("Honda", "CBR")
miMoto.caballito()
miMoto.estado()

miFurgoneta = Furgoneta("Renault", "Kangoo")
miFurgoneta.arrancar()
miFurgoneta.estado()
print(miFurgoneta.carga(True))

class BicicletaElectrica(VElectricos, Vehiculos):
	pass

mibicicleta = BicicletaElectrica("marcaBici", "modeloBici")




