import socket

HEADER = 64
PORT = 5051
FORMAT = 'utf-8'
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(a):
    msg = a.encode(FORMAT)
    msg_length = len(msg)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(msg)


def recd():
    message = client.recv(2048).decode(FORMAT)
    message = eval(message)
    print(message)
    a = max(message)
    a = str(a)
    send(a)


recd()
