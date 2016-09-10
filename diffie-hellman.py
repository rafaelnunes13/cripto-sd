import random

#No caso do exercicio foi solicitado que os valores fossem P = 23 e g = 8, pois devem ser primos entre si.
p = 23
g = 8

#Necessario gerar os valores aleatorios para "a" e "b", utilizando o limite de 5000 pois no Diffie Helmann geralmente utilizasse numeros grandes.
a = random.randrange(1, 5000)
b = random.randrange(1, 5000)

#Geracao das chaves consideradas "Publicas" que seriam trocadas entre as maquinas
A = (g**a)%p
B = (g**b)%p

#Utilizando a chave "Privada" gerada aleatoriamente um calcula a chave do outro
ka = (B**a)%p
kb = (A**b)%p

print "Chave A = %d" % ka
print "Chave B = %d" % kb

#Caso as chaves sejam iguais a operacao ocorreu corretamente, sendo possivel que um decifre a mensagem do outro
if ka == kb:
	print "Chaves geradas corretamente"	  
else:
	print "Chaves geradas incorretamente"