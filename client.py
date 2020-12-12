import socket

HOST = '127.0.0.1'  # Host para conexão
PORT = 65432        # Porta usada pelo server

#Conexão com o servidor
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    #Servidor devolve nomes que estão no arquivo JSON
    nomes = eval(s.recv(1024).decode('utf-8'))
    #Nomes aparecem para decidir sobre qual quer mais informações
    print("\nDigite o código do usuário para obter mais informações: ")
    print("  Código | Nome")
    i = 1
    for nome in nomes:
        print("     %d   | %s " %(i, nomes[nome]))
        i+=1
    #Decisão é salva e enviada para o server
    request = str(input('\n'))
    s.sendall(request.encode('utf-8'))
    #server devolve informações requiridas
    data = s.recv(1024).decode('utf-8')
#Informações são imprimidas
print('Dados:', data)