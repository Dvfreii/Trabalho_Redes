# -*- coding: utf-8 -*-
import socket

IP= 'localhost'
PORT= 5000
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = (IP, PORT)

while True:
    message = input("Digite uma mensagem: ")
    client_socket.sendto(str.encode(message), server_address)
        
    msg, _ = client_socket.recvfrom(1024)
    print("Resposta recebida do servidor :", str(msg.decode()))

