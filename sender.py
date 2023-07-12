import socket
import os
import keyboard


PATH = "./files/"


if __name__ == "__main__":
    sock = socket.socket()
    sock.connect(('localhost', 9090))


    files = list(os.walk("./files"))[0][2]
    while not keyboard.is_pressed("q"):
        n_files = list(os.walk("./files"))[0][2]
        for file in n_files:
            if file not in files:
                with open(f"{PATH}{file}", "r") as f:
                    data = f";{file}\n" + f.read()

                sock.send(str.encode(data))
        files = n_files

    sock.close()
