import socket


PATH = "./send/"
END_SIGN = "\n;kontz124534_per"

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)
conn, addr = sock.accept()


print('connected:', addr)

while True:

    fst = True
    name = ""

    l = []

    while "".join(l)[-len(END_SIGN):] != END_SIGN:
        data = conn.recv(1460)
        conn.send(b'o')
        if fst:
            name = data.decode().split("\n")[0][1:]
            print(name)

            f1 = open(f"{PATH}{name}", "w", encoding="utf-8")
            f1.write("")
            f1.close()

            file = open(f"{PATH}{name}", "a", encoding="utf-8")
            fst = False

        d_data = data.decode(encoding="utf-8")
        l = l[1:] + [d_data]
        file.write(d_data)
    conn.send(b'a')
    file.close()


conn.close()