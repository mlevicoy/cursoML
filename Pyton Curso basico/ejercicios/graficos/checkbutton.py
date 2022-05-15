from tkinter import *

root = Tk()

root.title("Ejemplo")

playa = IntVar()
montana = IntVar()
turismoRural = IntVar()

def opcionesViaje():
	opcionEscogida = ""
	if playa.get() == 1:
		opcionEscogida += " Playa"
	if montana.get() == 1:
		opcionEscogida += " Montaña"
	if turismoRural.get() == 1:
		opcionEscogida += " Turismo Rural"
	textoFinal.config(text=opcionEscogida)

foto = PhotoImage(file="mouse.gif")
Label(root, image=foto).pack()

frame = Frame(root)
frame.pack()

Label(frame, text="Elegir destinos", width=50).pack()

Checkbutton(frame, text="Playa", variable=playa, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(frame, text="Montaña", variable=montana, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(frame, text="Turismo Rural", variable=turismoRural, onvalue=1, offvalue=0, command=opcionesViaje).pack()

textoFinal = Label(frame)
textoFinal.pack()

root.mainloop()




