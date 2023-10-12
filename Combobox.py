import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.title("DE DONDE ERES?")
ventana.configure(bg='lavender')
ventana.geometry("300x200")

def seleccionar_opcion():
    opcion_seleccionada = combo.get()
    etiqueta_resultado.config(text=f"Seleccionaste: {opcion_seleccionada}")

#COMBO BOX 
opciones = ["Cholula", "Nealtican","Puebla","Zacatepec","Tepontla","Otro."]
combo = ttk.Combobox(ventana, values=opciones)
combo.pack(pady=10)
combo.set(opciones[0]) 

#NUESTRO BOTON
boton = ttk.Button(ventana, text="Obtener Selección", command=seleccionar_opcion)
boton.pack(pady=10)

#NESTRA ETIQUETA DE RESULTADO
etiqueta_resultado = ttk.Label(ventana, text="")
etiqueta_resultado.pack(pady=10)

ventana.mainloop()