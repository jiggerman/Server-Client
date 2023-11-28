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
    try:
        while True:
            message = input()
            send_message(message)
    except:
        print(f"Connection is broken!")
        client.send("Error".encode(FORMAT))
        client.close()


if __name__ == '__main__':
    start()