# -*- coding: utf-8 -*-
import socket

# Cria o socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
IP= 'localhost'
PORT= 5000

server_socket.bind((IP, PORT))
print("Servidor iniciado. Aguardando solicitações...")

while True:
    MSG, client_address = server_socket.recvfrom(1024)
    print("Solicitação recebida do cliente:", client_address)
    PRINT= str(MSG, 'utf-8')
        
    resposta = input("Digite uma mensagem para cliente: ")
    server_socket.sendto(str.encode(resposta), client_address)
           
    
            