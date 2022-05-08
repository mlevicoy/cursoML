from tkinter import *

root = Tk()

miFrame = Frame(root, width=500, height=400)

miFrame.pack()

# Si se usa la variable
miLabel = Label(miFrame, text="Hola alumnos de Python")
miLabel.place(x=100, y=200)

# Si no se usa la variable
Label(miFrame, text="Hola alumnos de Python", fg="red", font=("Comic Sans MS", 18)).place(x=100, y=200)

# Colocar una imagen 
miImagen = PhotoImage(file="mouse.gif")
Label(miFrame, image=miImagen).place(x=100, y=200)

root.mainloop()


