viagem = int(input("Qual foi a distância ?"))
if viagem >= 200:
    maiorDistancia = viagem * 0.45
    print("O valor cobrado será de R$",maiorDistancia)
else:
    pequenaDistancia = viagem * 0.50
    print("O valor cobrado será de R$",pequenaDistancia)