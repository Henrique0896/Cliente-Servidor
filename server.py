from socket import socket, AF_INET, SOCK_STREAM
from json import load

HOST = '127.0.0.1'  # Host para conexão
PORT = 65432        # Porta ouvinte

#Carrega as informações do arquivo json
with open('users.json', 'r') as json_file:
    dados = load(json_file)
    users = dados["users"]

#Cria uma str de nomes para apresentação imediata
nomes = dict()
for user in users:
    nomes[user] = users[user]['name']
nomes = str(nomes).encode('utf=8')

#Faz conexão com o cliente
with socket(AF_INET,SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        #mostra quem conectou
        print('Connected by', addr)
        #devolve nomes do arquivo json
        conn.sendall(nomes)
        while True:
            #recebe opção do user
            opt = conn.recv(1024)
            if not opt:
                break
            opt = opt.decode('utf-8')
            data = str(users[opt]).encode('utf=8')
            #devolve as informações requeridas
            conn.sendall(data)