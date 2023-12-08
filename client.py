import socket 
import threading
import time
import json

PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT!'
SERVER = '192.168.1.70'
ADDRES = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDRES)

data = {
    "name": ADDRES,
    "message": None
}


def catch_message():
    connect = True

    while connect:
        try:
            while True:
                msg = json.loads(client.recv(1024).decode())
                if msg:
                    print("Received: {}".format(msg))

                time.sleep(0.2)
        except:
            connect = False


def send_message():
    connect = True
    
    while connect:
        try:
            message = input()
            if message:
                data['message'] = message
                client.send((json.dumps(data)).encode(FORMAT))
                print("Sent: {}".format(data))

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