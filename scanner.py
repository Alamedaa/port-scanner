import socket
from sys import argv

# Creditos:Alameda


# uso try e except pra capturar o erro e informa ao usuario modo de uso do script
# try e except eh usado para capturar e manipular excecoes
# try age na parte "normal" do programa. Codigo except eh a resposta do programa a qual quer erro

try:
	# faco um range pra regar portas do 1 ate 65535 "Limite de porta eh ate 65535"
	for porta in range(1,65535):
		# Faco um socket de tcp
		c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		c.settimeout(0.1) #  Uso settimeout para nao fica esperando muito tempo se porta nao da resultado de = 0
		if c.connect_ex((argv[1],porta)) == 0: # Verifico se a conexao do alvo e porta da igual 0, se for igual 0 eh por que esta aberta 
			print(f"PORTA: {porta} {socket.getservbyport(porta)} ABERTA [+]") # Imprimo na tela
except Exception as Error: # Uso except pra mostra na tela o erro e mensagem do uso do script pro usuario
	print("Scanner De Portas\nModo de uso python3 script www.url.com\nSaida do erro >> ",Error," <<")
