import socket
import threading
import json
from calculate import *

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDRES = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT!'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDRES)

clients = []


def handle_client(conn, adress):
    try:
        print(f"Connection with {adress} was successful")

        if adress not in clients:
            clients.append(adress)

        connection = True

        while connection:
            data = json.loads(conn.recv(1024).decode())
            msg = data.get("message")

            if msg:
                if msg == 'Error':
                    connection = False
                    clients.pop(clients.index(adress))
                    break

                if (msg == DISCONNECT_MESSAGE):
                    connection = False
                    print(f"Connection with {adress} successfully terminated")
                    break

                data["name"] = "Server"

                if (calculate(msg)):
                    answer = str(calculate(msg))
                    data["message"] = answer
                    conn.send((json.dumps(data)).encode(FORMAT))
                else:
                    conn.send((json.dumps(data)).encode(FORMAT))

                print("Sent: {}".format(data))

        clients.pop(clients.index(adress))
        conn.close()

    except:
        print(f"Connection with {adress} is broken!")
        conn.close()


def start():
    server.listen()
    print(f"Listening server: {SERVER}")
    while True:
        conn, adress = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, adress))
        thread.start()
        print(f"Now active connection: {threading.active_count() - 1}")
        print(clients)


if __name__ == '__main__':
    print('[ SERVER - ACTIVE ]')
    start()
    