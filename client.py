import socket

def start_client(host, port, message):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    # Send data to the server
    bytes_sent = 0
    while bytes_sent < len(message):
        sent = client_socket.send(message[bytes_sent:].encode())
        if sent == 0:
            raise RuntimeError("Socket connection broken")
        bytes_sent += sent

    # receive the response from the server
    received_data = b""
    while True:
        data = client_socket.recv(1024)
        if not data:   #check for data available
            break
        received_data += data

    received_message = received_data.decode()
    print(f"Received from server: {received_message}")

    client_socket.close()

if __name__ == "__main__":
    HOST = '127.0.0.1'
    PORT = 55000
    MESSAGE = "Hello, from client to server!!! "
    start_client(HOST, PORT, MESSAGE)
