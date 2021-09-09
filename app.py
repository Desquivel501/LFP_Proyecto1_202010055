
from tkinter.constants import ANCHOR
from Analizador_Lexico import AnalizadorLexico as AL
from Analizador_Sintactico import AnalizadorSintactico as AS
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.filedialog import askopenfilename
import os.path

from PIL import ImageTk, Image 

cadena = ""
nombre = ""

def leer(): 
    filename = askopenfilename()
    archivo = open(filename, 'r')
    contenido = archivo.read()
    archivo.close()
    global cadena
    cadena = contenido
    
def escribir (ruta, contenido):
    archivo = open(ruta, 'w+')
    archivo.write(contenido)
    archivo.close()
    

def analizar():
    scanner = AL()
    analisis = AS()
    lista = scanner.analizar(cadena)
    # scanner.impTokens()
    # scanner.impErrores()
    lista_imagenes = analisis.analizar(lista)
    
    nombres = []
    for i in lista_imagenes:
        nombres.append(i.get_titulo().replace('"',""))
    
    cb_imagenes["values"] = nombres

def seleccionImagen(event):
    global nombre
    nombre = cb_imagenes.get()
    print(nombre)

def original():
    for widget in fr_imagen.winfo_children():
        widget.destroy()
    
    global img
    exist = os.path.isfile("Imagenes\\" + nombre + ".png")
    
    if exist:
        image = Image.open("Imagenes\\" + nombre + ".png") 
        img = ImageTk.PhotoImage(image)      
        label = tk.Label(fr_imagen, width = 575, height = 500, image=img, bg="#999999")
        label.image = img
        label.pack()

    else:
        image = Image.open("Imagenes\\not_found.png") 
        img = ImageTk.PhotoImage(image)      
        label = tk.Label(fr_imagen, width = 575, height = 500, image=img, bg="#999999")
        label.image = img
        label.pack()

def mirrorx():
    for widget in fr_imagen.winfo_children():
        widget.destroy()
    
    global img
    exist = os.path.isfile("Imagenes\\" + nombre + "_MIRRORX.png")
    
    if exist:
        image = Image.open("Imagenes\\" + nombre + "_MIRRORX.png") 
        img = ImageTk.PhotoImage(image)      
        label = tk.Label(fr_imagen, width = 575, height = 500, image=img, bg="#999999")
        label.image = img
        label.pack()

    else:
        image = Image.open("Imagenes\\not_found.png") 
        img = ImageTk.PhotoImage(image)      
        label = tk.Label(fr_imagen, width = 575, height = 500, image=img, bg="#999999")
        label.image = img
        label.pack()

def mirrory():
    for widget in fr_imagen.winfo_children():
        widget.destroy()
    
    global img
    exist = os.path.isfile("Imagenes\\" + nombre + "_MIRRORY.png")
    
    if exist:
        image = Image.open("Imagenes\\" + nombre + "_MIRRORY.png") 
        img = ImageTk.PhotoImage(image)      
        label = tk.Label(fr_imagen, width = 575, height = 500, image=img, bg="#999999")
        label.image = img
        label.pack()

    else:
        image = Image.open("Imagenes\\not_found.png") 
        img = ImageTk.PhotoImage(image)      
        label = tk.Label(fr_imagen, width = 575, height = 500, image=img,bg="#999999")
        label.image = img
        label.pack()

def doublemirror():
    for widget in fr_imagen.winfo_children():
        widget.destroy()
    
    global img
    exist = os.path.isfile("Imagenes\\" + nombre + "_DOUBLEMIRROR.png")
    
    if exist:
        image = Image.open("Imagenes\\" + nombre + "_DOUBLEMIRROR.png") 
        img = ImageTk.PhotoImage(image)      
        label = tk.Label(fr_imagen, width = 575, height = 500, image=img, bg="#999999")
        label.image = img
        label.pack()

    else:
        image = Image.open("Imagenes\\not_found.png") 
        img = ImageTk.PhotoImage(image)      
        label = tk.Label(fr_imagen, width = 575, height = 500, image=img, bg="#999999")
        label.image = img
        label.pack()



if __name__ == '__main__':
    
    window = tk.Tk()
    window.geometry("800x600")
    window.title("Bitxelart")
    window.resizable(width=False, height=False)
    
    btn_cargar = tk.Button(window, text="Cargar", width=10, command=leer)
    btn_cargar.place(x = 10, y = 10)

    btn_analizar = tk.Button(window, text="Analizar", width=10, command=analizar)
    btn_analizar.place(x = 100, y = 10)
    
    btn_reportes = tk.Button(window, text="Reportes", width=10)
    btn_reportes.place(x = 190, y = 10)
    
    btn_salir = tk.Button(window, text="Salir", width=10)
    btn_salir.place(x = 280, y = 10)
    
    cb_imagenes = ttk.Combobox(window, values=[], width=20, font = "Arial 12 bold")
    cb_imagenes.place(x = 370, y = 10)
    cb_imagenes.bind("<<ComboboxSelected>>", seleccionImagen)
    
    
    fr_main = tk.Frame(window, width=780, height=545, relief=tk.GROOVE, bd=2)
    fr_main.place(x = 10, y = 45)
    
    fr_filtro = tk.Frame(fr_main, width=200, height=525, relief=tk.GROOVE, bd=2)
    fr_filtro.place(x = 15, y = 175)
    
    fr_imagen = tk.Frame(fr_main, width=580, height=515, relief=tk.GROOVE, bd=2, bg="#999999")
    fr_imagen.place(x = 175, y = 15)
    
    
    radioValue = tk.IntVar() 
    rdioOne = tk.Radiobutton(fr_filtro, text='Original', width=18, pady=(10), variable=radioValue, value=1, indicatoron=False, command=original, selectcolor="#64b2e7")
    rdioTwo = tk.Radiobutton(fr_filtro, text='MIRRORX', width=18, pady=(10),variable=radioValue, value=2, indicatoron=False, command=mirrorx,selectcolor="#64b2e7") 
    rdioThree = tk.Radiobutton(fr_filtro, text='MIRRORY', width=18, pady=(10),variable=radioValue, value=3, indicatoron=False, command=mirrory,selectcolor="#64b2e7")
    rdioFour = tk.Radiobutton(fr_filtro, text='DOUBLEMIRROR', width=18, pady=(10),variable=radioValue, value=4, indicatoron=False, command=doublemirror,selectcolor="#64b2e7")

    rdioOne.grid(column=0, row=0, sticky="W")
    rdioTwo.grid(column=0, row=1, sticky="W")
    rdioThree.grid(column=0, row=2, sticky="W")
    rdioFour.grid(column=0, row=3, sticky="W")
    

    window.mainloop()
