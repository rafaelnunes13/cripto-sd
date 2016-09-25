import random
from simplecrypt import encrypt, decrypt

#Funcao para encontrar numero primo aleatorio dentro de um range
def randomPrimo(ini, fim):
	nrPrimo = random.randrange(ini, fim)
	ehPrimo = 0
	contPrimo = 0

	while ehPrimo == 0:
		i = 1
		while i < 6:
			i += 1
			if ((i**(nrPrimo-1)) % nrPrimo) == 1:
				contPrimo += 1
			else:
				i = 6

		if contPrimo == 5:
			ehPrimo = 1
		else:
			ehPrimo = 0
			contPrimo = 0
			nrPrimo = random.randrange(ini, fim)

	#print "%d ? %d" % (nrPrimo, ehPrimo)

	return nrPrimo

#No caso do exercicio foi solicitado que os valores fossem P = 23 e g = 8, pois devem ser primos entre si.
#p = 23
#g = 8

p = randomPrimo(2, 2048)
g = randomPrimo(1, p-1)

bitsChave = 0

while bitsChave != 8 and bitsChave != 16 and bitsChave != 32 and bitsChave != 64 and bitsChave != 128:
	bitsChave = input("Informe o tamanho da chave que deseja utilizar (8, 16, 32, 64, 128): ")

chaveMax = (2**bitsChave)-1

a = random.randrange(1, chaveMax)
b = random.randrange(1, chaveMax)

#Necessario gerar os valores aleatorios para "a" e "b", utilizando o limite de 5000 pois no Diffie Helmann geralmente utilizasse numeros grandes.
#a = random.randrange(1, 5000)
#b = random.randrange(1, 5000)

print "Gerando chaves publicas"
#Geracao das chaves consideradas "Publicas" que seriam trocadas entre as maquinas
A = pow(g, a, p)
B = pow(g, b, p)

#Utilizando a chave "Privada" gerada aleatoriamente um calcula a chave do outro
ka = pow(B, a, p)
kb = pow(A, b, p)

#print "Chave A = %d" % ka
#print "Chave B = %d" % kb

#Caso as chaves sejam iguais a operacao ocorreu corretamente, sendo possivel que um decifre a mensagem do outro
if ka == kb:
	print "Chaves geradas corretamente"
else:
	print "Chaves geradas incorretamente"

msg = raw_input("Digite a mensagem para enviar para 'B': ")

#criptografa a mensagem
print "Criptografando mensagem em A..."
msgEnc = encrypt(str(ka), msg)

#descriptografa a partir da mensagem encriptada
print "Descriptografando mensagem em B..."
msgDec = decrypt(str(kb), msgEnc)

print "Mensagem de A decifrada em B:"
print msgDec