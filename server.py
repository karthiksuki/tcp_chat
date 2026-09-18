import socket   # Netowrk connections 
import threading # To perform vartious tasks at the same time 

# Configuration
host = "localhost" 
port = 5500 

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server.bind((host, port))
server.listen()

clients = []
nicknames = []


def broadcast(msg): 
    for client in clients: 
        client.send(msg) 


def handle(client): 
    while True: 
        try: 
            msg = client.recv(1024)
            broadcast(msg)
        except: 
            index = clients.index(client)
            clients.remove(client)
            client.close() 
            nickname = nicknames[index]
            broadcast('{} left!'.format(nicknames).encode('ascii'))
            nicknames.remove(nickname)
            break

def receive():
    while True:
        client, address = server.accept()
        print("Connected with {}".format(str(address)))

        client.send('NAME'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)
        print("Nickname is {}".format(nickname))
        broadcast("{} joined!".format(nickname).encode('ascii'))
        client.send('Connected to server!'.encode('ascii'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


if __name__ == "__main__":
    print(f"Server listening on {host}:{port}")
    receive()


