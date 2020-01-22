import socket
from _thread import start_new_thread

ip = '127.0.0.1'
port = 2424
buffer_size = 1024

def client_connect(connection):
   try:
       while True:
           data = connection.recv(buffer_size)
           if data == "exit":
               break
           decoded_text = data.decode("utf-8") 
           connection.send(str.encode(decoded_text))
   finally:
       connection.close()

def start_server():
   print('starting server...')
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   s.bind((ip, port))
   s.listen(1)
   while True:
       connection, address = s.accept()
       start_new_thread(client_connect, (connection,))

if __name__ == '__main__':
   start_server()