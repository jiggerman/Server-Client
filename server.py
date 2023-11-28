import socket
import threading

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT!'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

clients = []


def handle_client(conn, adress):
    try:
        print(f"Connection with {adress} was successful")

        if adress not in clients:
            clients.append(adress)

        connection = True
        while connection:
            msg = conn.recv(1024).decode()
            if (msg == DISCONNECT_MESSAGE):
                connection = False
                print(f"Connection with {adress} successfully terminated")
                break

            print(f"[ {adress} ] : {msg}")

        conn.close()

    except:
        print(f"Connection with {adress} is broken!")
        conn.close()


def start():
    server.listen()
    while True:
        conn, adress = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, adress))
        thread.start()
        print(f"Now active connection: {threading.activeCount() - 1}")
        print(clients)


if __name__ == '__main__':
    print('[ SERVER - ACTIVE ]')
    start()
    