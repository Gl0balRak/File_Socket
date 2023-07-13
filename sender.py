import socket
import os
import keyboard
from time import perf_counter


PATH = "./files/"


if __name__ == "__main__":
    sock = socket.socket()
    sock.connect(('localhost', 9090))


    files = list(os.walk("./files"))[0][2]
    while not keyboard.is_pressed("q"):
        n_files = list(os.walk("./files"))[0][2]
        for file in n_files:
            if file not in files:
                with open(f"{PATH}{file}", "r", encoding='utf-8') as f:
                    data = f";{file}\n" + f.read() + "\n;kontz124534_per"

                print(f"Start data translation {PATH}{file}")
                sock.send(str.encode(data))

                size = os.path.getsize(f"{PATH}{file}")
                cur_data_size = 0
                i = 0

                start = perf_counter()

                print(" ", end="")
                while cur_data_size < size:
                    resp = sock.recv(1).decode()

                    if resp == "o":
                        cur_data_size += 1460
                    else:
                        cur_data_size = size+100

                    percent = cur_data_size / size

                    s = round(percent * 20)
                    try:
                        time_e = (perf_counter() - start) / percent - perf_counter() + start
                    except ZeroDivisionError:
                        time_e = 0

                    print("\r" + "█" * s + " " * (20 - s) + f" {percent * 100:.2f}%" + f" time passed: {perf_counter() - start:.2f}; time estimated: {time_e:.2f}; average speed: {cur_data_size/(perf_counter() - start)/1024:0.2f} kB/s;",
                          end="")  # , end="\r")
                print("\n------------")



        files = n_files

    sock.close()
