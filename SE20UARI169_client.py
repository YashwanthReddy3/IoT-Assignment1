import socket

def main():
    server_ip = "10.59.238.168"
    server_port = 5000
    message = "Hello, Yashwanth to server"

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))
    client_socket.send(message.encode('utf-8'))
    response = client_socket.recv(1024).decode('utf-8')
    print(response)
    client_socket.close()

if __name__ == "__main__":
    main()
