# Import socket module
from socket import *    
import sys

# Create a TCP server socket
#(AF_INET is used for IPv4 protocols)
#(SOCK_STREAM is used for TCP)

serverSocket = socket(AF_INET, SOCK_STREAM)

# Assign a port number
serverPort = 9090

# Bind the socket to server address and server port
serverSocket.bind(("127.0.0.1", serverPort))

# Listen to at most 1 connection at a time
serverSocket.listen(1)

# Server should be up and running and listening to the incoming connections
while True:
	print ('Tudo pronto...')
	
	# Set up a new connection from the client
	connectionSocket, addr = serverSocket.accept()
	
	# If an exception occurs during the execution of try clause
	# the rest of the clause is skipped
	# If the exception type matches the word after except
	# the except clause is executed
	try:
		# Recebe a mensagem de solicitação do cliente
		message =  connectionSocket.recv(1024)
		#Extraia o caminho do objeto solicitado da mensagem
		# O caminho é a segunda parte do cabeçalho HTTP, identificado por [1]
		filename = message.split()[1]
		# porque o caminho extraído da solicitação HTTP inclui
		# um caractere '\', lemos o caminho do segundo caractere 
		f = open(filename[1:])

		# Armazene todo o conteúdo do arquivo solicitado em um buffer temporário
		outputdata = f.read()

		# Envie a linha de cabeçalho de resposta HTTP para o soquete de conexão
		connectionSocket.sendall(bytes('HTTP/1.1 200 OK\r\n\r\n','UTF-8'))
 
		# Envie o conteúdo do arquivo solicitado para o soquete de conexão
		for i in range(0, len(outputdata)):
			string = outputdata[i]
			dataBytes = string.encode("utf-8")
			connectionSocket.sendall(dataBytes)
			string2 = "\r\n"
			dataBytes2 = string2.encode("utf-8")
		connectionSocket.send(dataBytes2)
		
		# Close the client connection socket
		connectionSocket.close()
	except IOError:
		# Send HTTP response message for file not found
		#connectionSocket.send(bytes("HTTP/1.1 404 Not Found\r\n\r\n"))
		string="HTTP/1.1 404 Not Found\r\n\r\n"
		dataBytes = string.encode("utf-8")
		connectionSocket.send(dataBytes)
		string="<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n"
		dataBytes = string.encode("utf-8")
		connectionSocket.send(dataBytes)

		# Close the client connection socket
		connectionSocket.close()
	serverSocket.close()  
	sys.exit(1)

