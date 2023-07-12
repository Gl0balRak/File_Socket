import socket


PATH = "./send/"

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)
conn, addr = sock.accept()


print('connected:', addr)

while True:
    data = conn.recv(102400000)

    name = data.decode().split("\n")[0]

    with open(f"{PATH}{name}", "wb") as f:
        f.write(data)

    if not data:
        break
    conn.send(b"ok")

conn.close()