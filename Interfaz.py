from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

window = tk.Tk()
window.title("Conteo y Probabilidad")
#window.geometry("1050x500")
window.minsize(width=1200, height=500)  # tamaño
window.attributes('-fullscreen',True)
window.fullScreenState = False

window.configure(bg = 'lavender')


def quitFullScreen():
   fullScreenState = False
   window.attributes("-fullscreen", window.fullScreenState)

#Button(window,text="Minimizar", command= quitFullScreen).place(x=200, y=10)
Button(window, text="Salir",command=window.destroy).place(x=300,y=10)

#donde se ingresa los datos de los dados
def opc_dados():
    def obtener_opciondado(*args):
       elementos = int(opcion.get())
       for i in range(elementos):
           label1 = tk.Label(window, text=f"|{elementos, i+1}|=")
           label1.place(x=50, y=300 + 20 * i)
           carita = int(opcionCaras.get())
           for j in range(carita):
               entry = tk.Entry(window, width=10)
               entry.place(x=100 + 70 * j, y=300 + 20 * i)

#Cantidad de dados
    labelcd = Label(window, text="Seleccione la cantidad de dados:")
    labelcd.place(x=50, y=160)
    cantidad = {'1':'1 Dado', '2':'2 Dados', '3':'3 Dados', '4':'4 Dados', '5':'5 Dados', '6':'6 Dados', '7':'7 Dados', '8':'8 Dados', '9':'9 Dados', '10':'10 Dados',
                '11':'11 Dados', '12':'12 Dados', '13':'13 Dados', '14':'14 Dados', '15':'15 Dados', '16':'16 Dados', '17':'17 Dados', '18':'18 Dados', '19':'19 Dados', '20':'20 Dados'}
    opcion = tk.StringVar()
    opcion.set('1')
    select = tk.OptionMenu(window, opcion, *cantidad.keys(), command=obtener_opciondado)
    select.place(x=50, y=180)

#Cantidad de caras de dados
    labelcara = Label(window, text="Seleccione cuantas caras tienen los dados:")
    labelcara.place(x=50, y=210)
    caras = {'1':'4 Caras', '2':'6 Caras', '3':'8 Caras', '4':'12 Caras', '5':'20 Caras'}
    opcionCaras = tk.StringVar()
    opcionCaras.set('1')
    select = tk.OptionMenu(window, opcionCaras, *caras.keys(),command=obtener_opciondado)
    select.place(x=50, y=230)

    #ButtonCd = Button(window, text="Aceptar")
   # ButtonCd.place(x=50, y=100)
#Imagen del dado
image = Image.open("Nueva carpeta/dados.jpg")
image = image.resize((100, 100), Image.ANTIALIAS)
imagetk = ImageTk.PhotoImage(image)
labelImg = Label(window, image=imagetk).place(x=50, y=20)
ButtonD = Button(window, text="DADOS", command=opc_dados).place(x=70, y=130)

#ingresan los datos de la ruleta
def ruletadatos():
    def obtener_opcionruleta(*args):
        elementos = int(opcionrcan.get())
        for i in range(elementos):
            label1 = tk.Label(window, text=f"|{elementos, i + 1}|=")
            label1.place(x=50, y=300 + 20 * i)
            lado = int(opcionrcara.get())
            for j in range(lado):
                entry = tk.Entry(window, width=10)
                entry.place(x=100 + 70 * j, y=300 + 20 * i)


    labelcd = Label(window, text="Seleccione la cantidad de ruletas")
    labelcd.place(x=700, y=160)
    cantidadR = {'1': '1 Ruleta', '2':'2 Ruletas', '3':'3 Ruletas', '4':'4 Ruletas', '5':'5 Ruletas', '6':'6 Ruletas', '7':'7 Datos', '8':'8 Datos', '9':'9 Datos', '10':'10 Datos',
        '11':'11 Datos', '12':'12 Datos', '13':'13 Datos', '14':'14 Datos', '15':'15 Datos', '16':'16 Datos', '17':'17 Datos', '18':'18 Datos', '19':'19 Datos',
        '20':'20 Datos'}
    opcionrcan = tk.StringVar()
    opcionrcan.set('1')
    select = OptionMenu(window, opcionrcan, *cantidadR.keys(), command=obtener_opcionruleta)
    select.place(x=700, y=180)

    labelcd = Label(window, text="Seleccione la cantidad de datos")
    labelcd.place(x=700, y=210)
    cantidad = {'1': '1 Ruleta', '2':'2 Ruletas', '3':'3 Ruletas', '4':'4 Ruletas', '5':'5 Ruletas', '6':'6 Ruletas', '7':'7 Datos', '8':'8 Datos', '9':'9 Datos', '10':'10 Datos',
        '11':'11 Datos', '12':'12 Datos', '13':'13 Datos', '14':'14 Datos', '15':'15 Datos', '16':'16 Datos', '17':'17 Datos', '18':'18 Datos', '19':'19 Datos',
        '20':'20 Datos'}
    opcionrcara = tk.StringVar()
    opcionrcara.set('1')
    select = OptionMenu(window, opcionrcara, *cantidad.keys(), command=obtener_opcionruleta)
    select.place(x=700, y=230)

    #ButtonCd = Button(window, text="Aceptar", command=obtener_opcion)
    #ButtonCd.place(x=700, y=260)

image1 = Image.open("Nueva carpeta/ruleta.jpg")
image1 = image1.resize((100, 100), Image.ANTIALIAS)
imagetk1 = ImageTk.PhotoImage(image1)
labelImg = Label(window, image=imagetk1).place(x=700, y=20)
ButtonR = Button(window, text="RULETA", command=ruletadatos).place(x=730, y=130)

window.mainloop()