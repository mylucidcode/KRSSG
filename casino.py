import socket
import threading
import random

HEADER = 64
PORT = 5051
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

# running a loop for the total rounds taken 4
b = []
for j in range(0, 4):
    rl = []
    for i in range(0, 9):
        n1 = random.randint(1, 52)
        rl.append(n1)  # forming a list of random integers in the given range every new time the loop runs
    print(rl)


    # forming an array of cards for every player
    def handle_player(conn1, addr1, n):

        l1 = []
        l1 = [rl[n], rl[n + 1], rl[n + 2]]
        l1 = str(l1)
        conn1.send(l1.encode(FORMAT))
        print(l1)
        l1 = []
        n = n + 3
        conn1.close()

    # receiving cards from every player in return and calculating maximum, printing for every round
    def calc(conn2, addr2):
        while True:
            a = []
            header = conn2.recv(HEADER).decode(FORMAT)
            msg_length=int(header)
            if msg_length:
                for n2 in range(0,3):
                    msg_length = int(msg_length)
                    msg = conn2.recv(msg_length).decode(FORMAT)
                    a[n2] = msg
                    print(msg)
            print(a)
            key = max(a)
            key2 = a.index(key)
            b.append(key2)
            a=[]
            print(f"Player {key2 + 1} is the winner of round {j + 1}")
        conn2.close()


    def start():
        server.listen()
        print("Server is listening")
        while True:
            conn, addr = server.accept()
            t1 = threading.Thread(target=handle_player, args=(conn, addr, 0))
            t1.start()
            conn1, addr1 = server.accept()
            t2 = threading.Thread(target=handle_player, args=(conn1, addr1, 3))
            t2.start()
            conn2, addr2 = server.accept()
            t3 = threading.Thread(target=handle_player, args=(conn2, addr2, 6))
            t3.start()
            break;
            print("This")


    def start2():
        server.listen()
        print("Server is listening2")
        while True:
            conn, addr = server.accept()
            t1 = threading.Thread(target=calc, args=(conn, addr))
            t1.start()
            conn1, addr1 = server.accept()
            t2 = threading.Thread(target=calc, args=(conn1, addr1))
            t2.start()
            conn2, addr2 = server.accept()
            t3 = threading.Thread(target=calc, args=(conn2, addr2))
            t3.start()
            break;


    start()
    start2()

flag = b.max()
print(f"Winner is player {flag + 1}")
