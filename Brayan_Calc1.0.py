from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from math import sqrt

ventana=Tk()
ventana.title("CALCULADORA_BDT")
ventana.configure(bg='lavender')

#i=0
#entrada
e_texto=Entry(ventana,font=("Calibri 20"))
e_texto.configure(bg="light gray")
e_texto.grid(row=0,column=0,columnspan=4,padx=5,pady=5)

i=0
def click_boton(valor):
    global i
    e_texto.insert(i,valor)
    i+=1
    
def borrar():
    e_texto.delete(0, END)
    i = 0
    
def eliminar():
    global i
    i=i-1
    e_texto.delete(i,END)
            
def operacion():
    ecuacion=e_texto.get()
    resultado=eval(ecuacion)
    e_texto.delete(0,END)
    e_texto.insert(0,resultado)
    i=0  
def convertir_hexadecimal():
    try:
        ecuacion = e_texto.get()
        resultado_decimal = eval(ecuacion)
        resultado_hexadecimal = hex(int(resultado_decimal))
        e_texto.delete(0, END)
        e_texto.insert(0, resultado_hexadecimal)
        global i
        i = 0
    except Exception as e:
        messagebox.showerror("Error", "¡AGREGA SOLO NUMEROS!")
        
def operacion_binaria(op):
    try:
        ecuacion = e_texto.get()
        resultado = eval(ecuacion)
        resultado_binario = bin(int(resultado))
        e_texto.delete(0, END)
        e_texto.insert(0, resultado_binario.upper())
        global i
        i = 0
    except Exception as e:
        messagebox.showerror("Error", "¡AGREGA SOLO NUMEROS!")

def x10():
    try:
        numero = float(e_texto.get())
        resultado = numero * 10
        e_texto.delete(0, END)
        e_texto.insert(0, resultado)
        global i
        i = 0
    except Exception as e:
        messagebox.showerror("Error", "¡AGREGA SOLO NUMEROS!")   
        
def raiz_cuadrada():
    try:
        numero = float(e_texto.get())
        resultado = sqrt(numero)
        e_texto.delete(0, END)
        e_texto.insert(0, resultado)
        global i
        i = 0
    except Exception as e:
        messagebox.showerror("Error", "¡AGREGA SOLO NUMEROS!") 
        
def Desactivar_hex_button():
    estado_actual = boton_convertir_hexadecimal.cget('state')
    nuevo_estado = 'normal' if estado_actual == 'disabled' else 'disabled'
    boton_convertir_hexadecimal.configure(state=nuevo_estado) 
        
              
    
boton1 = Button(ventana, text="1", width=5, height=2,command=lambda:click_boton(1), bg="white", font=("futura 9"))
boton2 = Button(ventana, text="2", width=5, height=2,command=lambda:click_boton(2), bg="white", font=("futura 9"))
boton3 = Button(ventana, text="3", width=5, height=2,command=lambda:click_boton(3), bg="white", font=("futura 9"))
boton4 = Button(ventana, text="4", width=5, height=2,command=lambda:click_boton(4), bg="white", font=("futura 9"))
boton5 = Button(ventana, text="5", width=5, height=2,command=lambda:click_boton(5), bg="white", font=("futura 9"))
boton6 = Button(ventana, text="6", width=5, height=2,command=lambda:click_boton(6), bg="white", font=("futura 9"))
boton7 = Button(ventana, text="7", width=5, height=2,command=lambda:click_boton(7), bg="white", font=("futura 9"))
boton8 = Button(ventana, text="8", width=5, height=2,command=lambda:click_boton(8), bg="white", font=("futura 9"))
boton9 = Button(ventana, text="9", width=5, height=2,command=lambda:click_boton(9), bg="white", font=("futura 9"))
boton0 = Button(ventana, text="0", width=5, height=2,command=lambda:click_boton(0), bg="white", font=("futura 9"))

boton_borrar = Button(ventana, text="AC", width=5, height=2,command=lambda:borrar(), bg="coral",font=("futura 8"))
boton_Parentesis1 = Button(ventana, text="(", width=5, height=2,command=lambda:click_boton("("), bg="azure", font=("futura 9"))
boton_Parentesis2 = Button(ventana, text=")", width=5, height=2,command=lambda:click_boton(")"), bg="azure", font=("futura 9"))
boton_Punto = Button(ventana, text=".", width=5, height=2,command=lambda:click_boton("."), bg="white")
boton_convertir_hexadecimal= Button(ventana, text="Hex", width=5, height=2,command=lambda:convertir_hexadecimal(), bg="light blue", font=("futura 8"))
boton_x10= Button(ventana, text="x10", width=5, height=2,command=lambda:x10(), bg="white", font=("futura 9"))
boton_potencia= Button(ventana, text="^", width=5, height=2,command=lambda:click_boton("^"), bg="coral")
boton_eliminar= Button(ventana, text="<-", width=5, height=2,command=lambda:eliminar(), bg="light blue")
boton_Desactivar_hex = Button(ventana, text="Block Hex", width=8, height=2, command=Desactivar_hex_button, bg="light blue",font=("futura 8"))
boton_raiz = Button(ventana, text="√", width=5, height=2, command=raiz_cuadrada, bg="light green", font=("futura 9"))
boton_and = Button(ventana, text="Bin", width=5, height=2, command=lambda: operacion_binaria('&'), bg="light blue",font=("futura 8"))
boton_div = Button(ventana, text="/", width=5, height=2,command=lambda:click_boton("/"), bg="azure", font=("futura 9"))
boton_mult = Button(ventana, text="x", width=5, height=2,command=lambda:click_boton("*"), bg="azure", font=("futura 9"))
boton_suma = Button(ventana, text="+", width=5, height=2,command=lambda:click_boton("+"), bg="azure", font=("futura 9"))
boton_resta = Button(ventana, text="-", width=5, height=2,command=lambda:click_boton("-"), bg="azure", font=("futura 9"))
boton_igual = Button(ventana, text="=", width=5, height=2,command=lambda:operacion(), bg="azure", font=("futura 9"))

#asignamos colocacion de elementos en ventana
boton_borrar.grid(row=1, column=0, padx=5, pady=5)
boton_eliminar.grid(row=1, column=3, padx=5, pady=5)
boton_Parentesis1.grid(row=2, column=1, padx=5, pady=5)
boton_Parentesis2.grid(row=2, column=2, padx=5, pady=5)
boton_div.grid(row=2, column=3, padx=5, pady=5)

boton7.grid(row=3, column=0, padx=5, pady=5)
boton8.grid(row=3, column=1, padx=5, pady=5)
boton9.grid(row=3, column=2, padx=5, pady=5)
boton_mult.grid(row=3, column=3, padx=5, pady=5)

boton4.grid(row=4, column=0, padx=5, pady=5)
boton5.grid(row=4, column=1, padx=5, pady=5)
boton6.grid(row=4, column=2, padx=5, pady=5)
boton_suma.grid(row=4, column=3, padx=5, pady=5)

boton1.grid(row=5, column=0, padx=5, pady=5)
boton_convertir_hexadecimal.grid(row=2, column=0, padx=5, pady=5)
boton2.grid(row=5, column=1, padx=5, pady=5)
boton3.grid(row=5, column=2, padx=5, pady=5)
boton_resta.grid(row=5, column=3, padx=5, pady=5)

boton_Desactivar_hex.grid(row=1, column=1, padx=5, pady=5)
boton_raiz.grid(row=6, column=2, padx=5, pady=5)
boton_and.grid(row=1, column=2, padx=5, pady=5)
boton0.grid(row=6, column=0, padx=5, pady=5)
boton_Punto.grid(row=6, column=1, padx=5, pady=5)
boton_igual.grid(row=6, column=3, padx=5, pady=5)


ventana.mainloop()