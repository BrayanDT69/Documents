import tkinter as tk
from tkinter import ttk


ventana = tk.Tk()
ventana.title("CONVERSOR")
ventana.configure(bg='Light Gray')
ventana.geometry("300x200")


def convertir():
    unidad_seleccionada = combo_unidades.get()
    valor = float(entrada_valor.get())
    
    if unidad_seleccionada == "Kilómetros a Millas":
        resultado = valor * 0.621371
    elif unidad_seleccionada == "Millas a Kilometros":
        resultado = valor /0.621371
    elif unidad_seleccionada == "Celsius a Fahrenheit":
        resultado = (valor * 9/5) + 32
    elif unidad_seleccionada == "Fahrenheit a Celcius":
         resultado = (valor - 32) * 5/9
    elif unidad_seleccionada == "Metros a Pies":
        resultado = valor * 3.28084
    else:
        resultado = "Seleccione una conversión válida"
    
    etiqueta_resultado.config(text=f"Resultado: {resultado}")


#COMBO BOX 
opciones = ["Kilómetros a Millas","Millas a Kilometros", "Celsius a Fahrenheit", "Fahrenheit a Celcius", "Metros a Pies"]
combo_unidades = ttk.Combobox(ventana, values=opciones)
combo_unidades.pack(pady=10)
combo_unidades.set(opciones[0]) 

#INGRESAMOS EL VALOR
entrada_valor = ttk.Entry(ventana)
entrada_valor.pack(pady=10)
entrada_valor.insert(0, "0") 

#NUESTRO BOTON
boton_convertir = ttk.Button(ventana, text="Convertir", command=convertir)
boton_convertir.pack(pady=10)

#NESTRA ETIQUETA DE RESULTADO
etiqueta_resultado = ttk.Label(ventana, text="")
etiqueta_resultado.pack(pady=10)


ventana.mainloop()