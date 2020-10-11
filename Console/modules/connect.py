import socket, threading
from Console.modules.TextColor import *
#globals

def Listen(host, port):
	Sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	Sock.bind((host, port))
	Sock.listen()

	conn, addr = Sock.accept()
