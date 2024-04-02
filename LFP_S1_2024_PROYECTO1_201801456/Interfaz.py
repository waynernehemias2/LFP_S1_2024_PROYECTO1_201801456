from distutils.command.config import config
from lib2to3.pgen2 import token
from string import hexdigits
from tkinter import *
from tkinter import filedialog
from tkinter.tix import ButtonBox, ComboBox
from turtle import width
from webbrowser import BackgroundBrowser
from matplotlib.pyplot import grid, text
from mysqlx import Row
import tkinter as tk

raiz = tk.Tk()
raiz2 = tk.Tk()
nuevoFrame = Frame(raiz, width=750, height=750)
nuevoFrame2 = Frame(raiz2, width=550, height=450)
cuadroTexto = Text(nuevoFrame, width=40, height=35 )
cuadroTexto2 = Text(nuevoFrame, width=40, height=35 )

ruta = ""
archivoLFP = ""
archivoCargado = ""
lista = ""
pruebas = ['Reporte tokens', 'Reporte de errores']

def inicio():
    global raiz2,nuevoFrame,cuadroTexto,cuadroTexto2
    raiz.title("Inicio")
    nuevoFrame.config(bg="red")
    nuevoFrame.pack()
    nuevoLabel = Label(nuevoFrame, text="Seleccione ruta de archivo", fg="blue").place(x=10, y=15)
    nuevoLabe2 = Label(nuevoFrame, text="Texto de entrada", fg="blue").place(x=40, y=60)
    nuevoLabe3 = Label(nuevoFrame, text="Traducción", fg="blue").place(x=390, y=60)
    cuadroTexto.place(x=40, y=90)
    cuadroTexto2.place(x=390, y=90)
    botonArchivo = Button(nuevoFrame, text="Abrir archivo", fg="black" ).place(x=170, y=15)
    botonAnalizar = Button(nuevoFrame, text="Traducir", fg="black").place(x=500, y= 15)
    botonReportes = Button(nuevoFrame, text="Menú reportes", fg="red", background="blue").place(x=650, y= 15)
    raiz.mainloop()

def cargarArchivo():
    global ruta, archivoCargado, archivoLFP
    print("")
    print("Cargue el archivo")
    ruta = filedialog.askopenfilename(title="Seleccione archivo LFP")
    if ruta != "":
        print("Se cargo con exito el archivo \nLa ruta es: "+ruta)
        archivoLeido = open(ruta, "r")
        archivoLFP =archivoLeido.readlines()
        archivoLeido.close()
        print(archivoLFP)           
        print("_______________________")
        print(" ")
    else:
        print("No se pudo cargar el archivo")
    cuadroTexto.insert(INSERT,archivoLFP)


inicio().__init__