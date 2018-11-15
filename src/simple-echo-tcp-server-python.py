import socket
from thread import start_new_thread

ip = '127.0.0.1'
port = 2424
buffer_size = 1024


def client_connect(connection):
    try:
        connection.send("Welcome to the Server. Type messages and press enter to send.\n")

        while True:
            data = connection.recv(buffer_size)
            if data == "exit":
                break

            connection.send(data * 2)
    finally:
        connection.close()


def start_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((ip, port))
    s.listen(1)

    while True:
        connection, address = s.accept()
        start_new_thread(client_connect, (connection,))
        