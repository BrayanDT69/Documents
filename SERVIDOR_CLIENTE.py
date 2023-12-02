import socket
import tkinter as tk

# Configuración del cliente
HOST = '192.168.68.228'
PORT = 65432

# Función para enviar datos al servidor
def enviar_comando(comando):
    client_socket.send(comando.encode())

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Cliente")

# Funciones para enviar comandos al servidor
def enviar_comando_1():
    enviar_comando("1")

def enviar_comando_2():
    enviar_comando("2")

def enviar_comando_3():
    enviar_comando("3")

# Botones en la interfaz gráfica
btn_1 = tk.Button(root, text="Comando 1", command=enviar_comando_1)
btn_1.pack()

btn_2 = tk.Button(root, text="Comando 2", command=enviar_comando_2)
btn_2.pack()

btn_3 = tk.Button(root, text="Comando 3", command=enviar_comando_3)
btn_3.pack()

# Configuración del socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

# Iniciar la interfaz gráfica
root.mainloop()