''' Nome: Davi Freire Azevedo | Matricula: 498905 '''
import socket

def divisivel(NUM):
    return NUM % 2 == 0  


def verifica(conexao):
    recebe = conexao.recv(1024).decode() 
    print('Numero: ',recebe)

    if len(recebe) > 10:
        resposta = str(recebe)
    else:
        if divisivel(int(recebe)):
            resposta = "PAR"
        else:
            resposta = "ÍMPAR"
    conexao.sendall(resposta.encode())
    conexao.close()

            

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
        verifica(conexao)
            

servidor()
            