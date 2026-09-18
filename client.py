import socket
import threading


host = "localhost"
port = 5500

nickname = input("Enter a name for the chat: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

def receiver(): 
    while True: 
        try: 
            msg = client.recv(1024).decode('ascii')
            if msg == "NAME": 
                client.send(nickname.encode('ascii'))
            else: 
                print(msg)
        except: 
            print("An error occured!")
            client.close() 
            break

def write(): 
    while True: 
        msg = '{} : {}'.format(nickname, input(''))
        client.send(msg.encode('ascii'))


receiver_thread = threading.Thread(target=receiver) 
receiver_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()


