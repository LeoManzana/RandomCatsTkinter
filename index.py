from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import requests


#--Datos de la API
url = "https://cataas.com/cat"
filename = "cat.jpg" #Guardar imagen como "cat.jpg"
r = requests.get(url)

#--Guaardar imagen al inicio
with open(filename,"wb") as f:
        f.write(r.content)

#--Crear ventana
root = Tk()
root.Title = "RandomCat"
root.geometry("500x450")
root.config(bg="khaki")
root.resizable(False,False)

#--Sacar la imagen del gato al inicio
Foto = Image.open(filename) #Abir imagen
Foto.thumbnail((250,250)) #Ajustar su tamaño
Foto = ImageTk.PhotoImage(Foto) #Guardarla

#--Hacer encabezado
Encabezado = Label(root, text = "RandomCat", font="consolas 25 bold", fg="purple", bg="khaki")
Encabezado.pack(pady=10)

#--Funcion de generar imagen
def Generar():
    r = requests.get(url) #Buscar una imagen nueva

    with open(filename,"wb") as f: #Guardar la imagen
        f.write(r.content)

    #Hacer lo mismo que se hace al inicio
    Foto = Image.open(filename) #Abrir imagen
    Foto.thumbnail((250,250)) #Redimenzinarla
    Foto = ImageTk.PhotoImage(Foto) #Guardarla

    lbl.configure(image=Foto) #Actualizar label que muestra la imagen
    lbl.image = Foto
    root.update()

#--Funcion de guardar la imagen
def Guardar():
    NombreGuardar = filedialog.asksaveasfile(mode='w', defaultextension=".jpg")
    if not NombreGuardar:
        return

    Fotocopiar = Image.open(filename)
    Fotocopiar.save(NombreGuardar)

#--Crear boton de generar
BotonP = Button(root,text="¡Generar!",font="arial 20", bg="spring green", fg="black",command=Generar)
BotonP.pack(padx=5,pady=50,side=BOTTOM)

#--Crear boton para guardar
BotonG = Button(root,text="Guardar",font="arial 15", bg="dark orange", fg="black",command=Guardar)
BotonG.place(x=200,y=400)

#--Crear la label que mostrara la imagen
lbl = Label(root, image = Foto)
lbl.pack()

#--Bucle de ventana
root.mainloop()