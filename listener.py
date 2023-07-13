import socket


PATH = "./send/"
END_SIGN = "kontz124534_per"

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)
conn, addr = sock.accept()


print('connected:', addr)

while True:

    text = ""
    fst = True
    name = ""
    while text[-len(END_SIGN):] != END_SIGN:

        data = conn.recv(1460)
        if fst:
            name = data.decode().split("\n")[0][1:]
            fst = False
        text += data.decode()

    text = text[:-len(END_SIGN)]

    with open(f"{PATH}{name}", "w", encoding="utf-8") as f:
        f.write(text)

conn.close()