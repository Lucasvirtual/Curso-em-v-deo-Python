import random
pc = random.randint(0,5)
numero = int(input("Acerte o número"))
print("o número que você escolheu",numero)
print("o número que o pc sorteou",pc)

if numero == pc:
    print("Você acertou")
else:
    print("você errou!")
