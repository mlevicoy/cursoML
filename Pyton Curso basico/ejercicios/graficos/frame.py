from tkinter import *

raiz = Tk()

raiz.title("Ventana de pruebas")

raiz.iconbitmap("gato.ico")

raiz.config(bg="blue")

# Tamaño borde
raiz.config(bd=45)
# Tipo de borde
raiz.config(relief="groove")
# Forma del cursor
raiz.config(cursor="hand2")

miFrame = Frame()

miFrame.pack(fill="both", expand="True")

miFrame.config(bg="red")

miFrame.config(width="650", height="350")

# Tamaño borde
miFrame.config(bd=35)
# Tipo de borde
miFrame.config(relief="sunken")
# Forma del cursor
miFrame.config(cursor="pirate")

raiz.mainloop()


