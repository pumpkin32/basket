import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("айпи адресс получателя", 2525))

with open("picture.png", "rb") as file:
	sock.send(file.read())
