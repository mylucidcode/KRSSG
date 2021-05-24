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
    def caly(a):
        key = max(a)
        key2 = a.index(key)
        b.append(key2)
        print(f"Player {key2 + 1} is the winner of round {j}")

    # forming an array of cards for every player
    def handle_player(conn1, addr1, n, a, n2):
        l1 = []
        l1 = [rl[n], rl[n + 1], rl[n + 2]]
        l1 = str(l1)
        conn1.send(l1.encode(FORMAT))
        l1 = []
        while True:
            header = conn1.recv(HEADER).decode(FORMAT)
            msg = conn1.recv(HEADER).decode(FORMAT)
            if msg:
                a[n2] = msg
                if (n2 == 2):
                    caly(a)
                    break
        conn1.close()

    def start():
        server.listen()
        a=[0, 0, 0]
        conn, addr = server.accept()
        t1 = threading.Thread(target=handle_player, args=(conn, addr, 0, a, 0))
        t1.start()
        conn1, addr1 = server.accept()
        t2 = threading.Thread(target=handle_player, args=(conn1, addr1, 3, a, 1))
        t2.start()
        conn2, addr2 = server.accept()
        t3 = threading.Thread(target=handle_player, args=(conn2, addr2, 6, a, 2))
        t3.start()
    start()

flag = max(b)
print(f"Winner is player {flag + 1}")
