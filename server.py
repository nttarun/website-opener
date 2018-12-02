import webbrowser
import socket


def server_program():
    host = socket.gethostname()
    port = 5000
    try:
        server_socket = socket.socket()
        print('socket created ')
    except:
        print('could not create socket')

    server_socket.bind((host, port))

    server_socket.listen(2)
    try:
        conn, address = server_socket.accept()
        print('connected with client')
    except:
        print('connection with client failed')
    print("Connection from: " + str(address))
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        webbrowser.open(data)

    conn.close()


if __name__ == '__main__':
    server_program()
