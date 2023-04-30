''' Nome: Davi Freire Azevedo | Matricula: 498905 '''
import socket
import random
import time

def gerador():
    gerar_num = str(random.randint(0, 10**30))
    return gerar_num



def cliente():
    print('Conectado ao servidor')
    while True:
        IP= '127.0.0.1'
        Port= 5000
        cliente= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cliente.connect((IP, Port))
        
        gerar = gerador()
        print("Número gerado:", gerar)

        cliente.sendall(gerar.encode())
        recebe= cliente.recv(1024).decode()
        print('Servidor recebeu: ', recebe)

        cliente.close()
        print("FIM")

        time.sleep(10)

   
cliente()
  



