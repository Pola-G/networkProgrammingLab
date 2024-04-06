import socket

def start_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Server listening on {host}:{port}...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address} established.")

        # Receive data from the client
        received_data = b""
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            received_data += data

        received_message = received_data.decode()
        print(f"Received message from client: {received_message}")

        # Echo the message back to the client
        client_socket.sendall(received_data)
        client_socket.close()

if __name__ == "__main__":
    HOST = '127.0.0.1'
    PORT = 55000
    start_server(HOST, PORT)
