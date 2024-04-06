import socket
import threading

# Connection Data
host = '127.0.0.1'
port = 7000

# Starting Server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

# Lists For Clients and Their Nicknames
clients = []
nicknames = []

# Sending Messages To All Connected Clients
def send_message(client, message):
    try:
        client.send(message)
    except:
        # If there's an issue with the client, remove them
        index = clients.index(client)
        clients.remove(client)
        nickname = nicknames[index]
        print(f"Removing {nickname} due to connection issue.")
        client.close()
        nicknames.remove(nickname)

# Handling Messages From Clients
def handle(client):
    while True:
        try:
            # Receiving message from the client
            message = client.recv(1024)
            if message:
                # Sending message to the same client
                send_message(client, message)
        except:
            # If there's an issue with the client, remove them
            index = clients.index(client)
            clients.remove(client)
            nickname = nicknames[index]
            print(f"Removing {nickname} due to connection issue.")
            client.close()
            nicknames.remove(nickname)
            break

# Receiving / Listening Function
def receive():
    while True:
        # Accept Connection
        client, address = server.accept()
        print("Connected with {}".format(str(address)))

        try:
            # Request And Store Nickname
            client.send('NICK'.encode('ascii'))
            nickname = client.recv(1024).decode('ascii')
            nicknames.append(nickname)
            clients.append(client)

            # Print And Broadcast Nickname
            print("Nickname is {}".format(nickname))
            client.send('Connected to server!'.encode('ascii'))

            # Start Handling Thread For Client
            thread = threading.Thread(target=handle, args=(client,))
            thread.start()
        except:
            # If there's an issue with the client, remove them
            print("Connection error with a client.")
            client.close()

receive()
