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



