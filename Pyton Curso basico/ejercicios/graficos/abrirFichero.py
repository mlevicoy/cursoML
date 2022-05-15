from tkinter import *
from tkinter import filedialog

root = Tk()

def abreFichero():
	fichero = filedialog.askopenfilename(title="Buscar archivo...",
		initialdir="C:", filetypes=(("Ficheros de Excel", "*.txt"),
			("Ficheros PDF", "*.pdf"), ("Ficheros de texto", "*.txt"),
			("Todos los fichero", "*.*")))
	print(fichero)

Button(root, text="Abrir fichero", command=abreFichero).pack()

root.mainloop()


