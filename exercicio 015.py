km = int(input("Quantos Km foi percorrido pelo carro ?"))
dias = int(input("Quantos dia ele foi alugado ?"))
dias1 = dias * 60
precoKm = km * 0.15
preco = dias1 + precoKm
print("O valor do aluguel foi de R${}".format(preco))