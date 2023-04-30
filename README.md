# Trabalho_Redes
Repositório para trabalho prático de redes 
Alunos: Davi Freire Azevedo
Matrícula: 498905

Descrição 
Programa Cliente
1. O programa cliente irá se conectar ao servidor; ok
2. Gerar um número inteiro com até 30 casas; ok
3. Enviar esse número para o servidor; ok
4. Deve receber, imprimir no console e devolver o valor recebido do servido + “FIM” ok
5. Fecha a conexão ok
Repete a cada 10 segundo ok

FUNÇOES CLIENTE:

gerar(): Esta função gera um número inteiro aleatório com até 30 dígitos. Ela utiliza a biblioteca random do Python para gerar o número e o retorna como uma string.

cliente(): Esta função inicia o cliente. Ela entra em um loop infinito e realiza as seguintes etapas:

Cria um objeto de socket (cliente).
Conecta-se ao servidor especificado pelo endereço IP e porta.
Gera um número aleatório usando gerar().
Imprime o número gerado no console.
Envia o número para o servidor usando send().
Recebe a resposta do servidor usando recv() e a decodifica de bytes para uma string.
Imprime a resposta recebida no console.
Envia a string "FIM" para indicar ao servidor que a comunicação foi concluída.
Fecha a conexão com o servidor.
Aguarda 10 segundos antes de repetir o processo.

Programa Servidor
1. O programa servidor irá esperar a conexão de clientes; ok
2. Recebe o número; ok 
3. Se o número tiver mais de 10 casas, gera e envia uma string do mesmo tamanho para o cliente; ok
4. Se for menor que 10, verifica se é par ou ímpar e envia “PAR” ou “ÍMPAR” para o cliente. ok

FUNÇOES SERVIDOR:

divisivel(NUM): Esta função verifica se um número é par ou ímpar. Ela recebe um número como entrada e retorna True se o número for par e False se for ímpar.

verifica(conexao): Esta função é responsável por lidar com a conexão de um cliente. Ela recebe um objeto de socket (cliente) que representa a conexão com o cliente. A função realiza as seguintes etapas:

Recebe o número enviado pelo cliente usando recv() e decodifica-o de bytes para uma string.
Imprime o número recebido no console.
Verifica o tamanho do número:
Se tiver mais de 10 dígitos, gera uma string do mesmo tamanho e a envia de volta ao cliente.
Se tiver menos de 10 dígitos, verifica se é par ou ímpar e envia a string "PAR" ou "ÍMPAR" de volta ao cliente.
Fecha a conexão com o cliente usando close().

servidor(): Esta função inicia o servidor. Ela cria um objeto de socket (servidor), vincula-o a um endereço IP e porta especificados e o coloca em modo de escuta. Em seguida, entra em um loop infinito em que aguarda a conexão de clientes. Quando uma conexão é estabelecida, chama a função verifica() para lidar com o cliente.

