import socket

host = '192.168.1.72 '
port = 1234

val = "Hi, i'm server"

def serverSetting():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print ('socket terbuat')
	try:
		s.bind((host, port))
	except socket.error as msg:
		print(msg)
	print('Socket bind selesai')
	return s 
	
def koneksiSetting():
	s.listen(1)
	conn, address = s.accept()
	print("koneksi ke: " +address[0] + ":" + str(address[1]))
	return conn
	
def AMBIL():
	reply = val
	return reply
	
def ULANG(dataMessage):
	reply = dataMessage[1]
	return reply
	
def dataTransfer(conn):
	while True:
		data = conn.recv(1024)
		data = data.decode('utf-8')
		
		dataMessage = data.split(' ', 1)
		command = dataMessage[0]
		if command == 'AMBIL':
			reply = AMBIL()
		elif command == 'ULANG':
			reply = ULANG(dataMessage)
		elif command == 'EXIT':
			print ('client telah off')
			break
		elif command == 'KILL':
			print('all off, bye')
			s.close()
			break
		else:
			reply = 'perintah tak diketahui'
			
		conn.sendall(str.encode(reply))
		print('data terkirim')
	conn.close()
	
s = serverSetting()

while True:
	try:
		conn = koneksiSetting()
		dataTransfer(conn)
	except:
		break
	
			
	
