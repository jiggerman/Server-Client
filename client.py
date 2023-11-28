import socket 

PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT!'
SERVER = '192.168.1.70'
ADDRES = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDRES)


def send_message(msg):
    message = msg.encode(FORMAT)
    client.send(message)


def start():
    while True:
        try:
            message = input()

            if message != DISCONNECT_MESSAGE:
                send_message(message)
            else:
                break
        except:
            print(f"Connection is broken!")


if __name__ == '__main__':
    start()