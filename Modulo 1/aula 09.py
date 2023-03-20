frase = "curso em video"

#remover espaços inuteis
print(frase.strip())

print(len(frase))
print(frase.count("o"))
print(frase.find("deo"))
print(frase[3])
#verificar se existe na frase
print("curso" in frase)

#trocar algo
print(frase.replace("curso","cu"))

#frase toda em maiuscula
print(frase.upper())

#primeira letra maiuscula
print(frase.capitalize())

#gera tecnicamente uma lista
print(frase.split())

print("-".join(frase))
