import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind( ('0.0.0.0', 1024) )

s.listen( 5 )

while True:
	clt, adr=s.accept()
	print(f"Connection to {adr} established")
	clt.send( bytes( "Socket Programming in Python", "utf-8" ) )
