import socket
import os

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("айпи адрес отправителя", 2525))

server.listen(5)


client = server.accept()


with open(os.path.join(os.getcwd(), "picture.png"), "wb") as file:
	while True:
		receiving = client[0].recv(1024)
		file.write(receiving)
