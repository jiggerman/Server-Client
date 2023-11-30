import socket 
import threading
import time

PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT!'
SERVER = '192.168.1.65'
ADDRES = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDRES)


def catch_message():
    connect = True

    while connect:
        try:
            while True:
                msg = client.recv(1024).decode()
                if msg:
                    print(msg)

                time.sleep(0.2)
        except:
            client.send("Error".encode(FORMAT))
            connect = False


def send_message():
    connect = True
    
    while connect:
        try:
            message = input()
            message = message.encode(FORMAT)
            client.send(message)
            time.sleep(0.2)
        except:
            connect = False
            print(f"Connection is broken!")
            client.send("Error".encode(FORMAT))
            


if __name__ == '__main__':
    thread = threading.Thread(target=catch_message)
    thread.start()
    send_message()
    client.close()