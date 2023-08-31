import socket

def main():
    server_ip = "10.59.238.168"
    server_port = 5000

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_ip, server_port))
    server_socket.listen(1)

    print("Server listening on {}:{}".format(server_ip, server_port))

    while True:
        client_socket, client_address = server_socket.accept()
        print("Connection from:", client_address)
        message = client_socket.recv(1024).decode('utf-8')
        print("Received message:", message)
        response = "Message received: {}".format(message)
        client_socket.send(response.encode('utf-8'))
        client_socket.close()

if __name__ == "__main__":
    main()
