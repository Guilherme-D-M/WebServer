# Importa o módulo de soquete
from socket import *    
import sys

# Cria um socket de servidor TCP
#(AF_INET é usado para protocolos IPv4)
#(SOCK_STREAM é usado para TCP)

serverSocket = socket(AF_INET, SOCK_STREAM)

# Atribui um número de porta
serverPort = 9090

# Vincula o soquete ao endereço do servidor e porta do servidor
serverSocket.bind(("127.0.0.1", serverPort))

# Ouve no máximo 1 conexão por vez
serverSocket.listen(1)

# O servidor vai estar funcionando e ouvindo as conexões de entrada
while True:
	print ('Tudo pronto...')
	
	# Configura uma nova conexão do cliente
	connectionSocket, addr = serverSocket.accept()
	
	# Se ocorrer uma exceção durante a execução da cláusula try
	# O resto da cláusula é ignorado
	# Se o tipo de exceção corresponder à palavra após exceto
	# A cláusula except é executada
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

		# Envia a linha de cabeçalho de resposta HTTP para o soquete de conexão
		connectionSocket.sendall(bytes('HTTP/1.1 200 OK\r\n\r\n','UTF-8'))
 
		# Envia o conteúdo do arquivo solicitado para o soquete de conexão
		for i in range(0, len(outputdata)):
			string = outputdata[i]
			dataBytes = string.encode("utf-8")
			connectionSocket.sendall(dataBytes)
			string2 = "\r\n"
			dataBytes2 = string2.encode("utf-8")
		connectionSocket.send(dataBytes2)
		
		# Fecha o soquete de conexão do cliente
		connectionSocket.close()
	except IOError:
		# Envia mensagem de resposta HTTP para arquivo não encontrado
		string="HTTP/1.1 404 Not Found\r\n\r\n"
		dataBytes = string.encode("utf-8")
		connectionSocket.send(dataBytes)
		string="<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n"
		dataBytes = string.encode("utf-8")
		connectionSocket.send(dataBytes)

		# Fecha o soquete de conexão do cliente
		connectionSocket.close()
	serverSocket.close()  
	sys.exit(1)
