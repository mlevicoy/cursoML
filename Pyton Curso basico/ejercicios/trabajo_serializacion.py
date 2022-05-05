import pickle

fichero = open("lista_nombres", "rb")

lista = pickle.load(fichero)

fichero.close()
del(fichero)

print(lista)

# lista_nombres = ["Pedro", "Ana", "María", "Isabel"]

# fichero_binario = open("lista_nombres", "wb")

# pickle.dump(lista_nombres, fichero_binario)

# fichero_binario.close()

# Borrado de memoria
# del(fichero_binario)

