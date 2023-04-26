# -*- coding: utf-8 -*-
import socket

IP= '127.0.0.1'
Port= 5000

cliente= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((IP, Port))


mensagem= input('Digite uma mensagem para o servidor: ')

while True:
    if  mensagem == 'sair':
        cliente.close()
        break
    elif(mensagem):
        cliente.sendall(str.encode(mensagem))
        
        recebe= cliente.recv(1024)
        print('Servidor disse: ', str(recebe,'utf-8'))
        mensagem= input('Digite uma mensagem para o servidor: ')
            
  



