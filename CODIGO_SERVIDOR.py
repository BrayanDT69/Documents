import socket
import serial
import threading

# Configuración del Arduino
arduino = serial.Serial('COM6', 9600)

# Configuración del servidor
HOST = '192.168.66.86'
PORT = 65432

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

def handle_client(client_socket):
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        arduino.write(data)
    client_socket.close()

while True:
    client, addr = server.accept()
    print(f'Conexión aceptada desde {addr[0]}:{addr[1]}')
    
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()
