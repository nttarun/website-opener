
import socket
import time


def client_program():
    host = socket.gethostname()
    port = 5000
    try:
        client_socket = socket.socket()
        print('socket creation is successful')
    except:
        print('socket creation was unsuccessful')
    try:
        client_socket.connect((host, port))
        print('connected to server')
    except:
        print('failed to connect with server')


    message = ['www.google.com','facebook.com','twitter.com','stackoverflow.com']

    for i in range(len(message)):
        client_socket.send(message[i].encode())
        time.sleep(3)


    client_socket.close()

if __name__ == '__main__':
    client_program()
