# -*- coding: utf-8 -*-
import socket

# Cria o socket
IP='localhost'
PORT=5000

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((IP, PORT))
servidor.listen(1)

print('Aguardando conexão de um cliente')

while True:
    # Recebe uma mensagem do cliente
    conexao, cliente = servidor.accept()
    print('Conectado em', cliente)
    
    while True:
        recebe = conexao.recv(1024) 
        if recebe:
            print(cliente, 'disse: ',str(recebe,'utf-8'))
            msg= input('Digite uma mensagem para o cliente: ')
            conexao.sendall(str.encode(msg))

        else:
            print('Fechando a conexão')
            conexao.close()
           
    
            