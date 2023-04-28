# -*- coding: utf-8 -*-
import socket


def servidor():
    IP='localhost'
    PORT=5000

    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((IP, PORT))
    servidor.listen(1)

    print('Aguardando conexão de um cliente')
    while True:
        conexao, cliente = servidor.accept()
        print('Conectado em', cliente)
        while True:
            recebe = conexao.recv(1024) 
           
            print(cliente, 'disse: ',str(recebe,'utf-8'))

            conexao.sendall(str.encode(str(recebe,'utf-8')))
servidor()
            