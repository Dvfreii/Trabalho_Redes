# -*- coding: utf-8 -*-
import socket
import random
import time

def gerador():
    gerar_num = random.randint(0, 10**30)
    return gerar_num



def cliente():
    IP= '127.0.0.1'
    Port= 5000
    cliente= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect((IP, Port))

    print('Conectado ao servidor')
    while True:
        
        gerar = gerador()
        cliente.sendall(str.encode(str(gerar)))
        recebe= cliente.recv(1024)
        print('Servidor recebeu: ', str(recebe,'utf-8'))

        time.sleep(10)

   
cliente()
  



