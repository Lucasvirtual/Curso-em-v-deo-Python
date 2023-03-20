import math
valor = float(input("Digite o ângulo que você deseja: "))
seno = math.sin(math.radians(valor))
print ("O ângulo de {} tem SENO de {:.2f}".format(valor,seno))
cosseno = math.cos(math.radians(valor))
print ("O ângulo de {} tem o COSSENO de {:.2f}".format(valor,cosseno))
tangente = math.tan(math.radians(valor))
print ("O ângulo de {} tem o TANGENTE de {:.2f}".format(valor, tangente))