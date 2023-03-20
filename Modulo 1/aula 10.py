nome = str(input("Qual seu nome ?"))
nota1 = float(input("Digite sua primeira nota"))
nota2 = float(input("Digite sua segunda nota"))
media = (nota1 + nota2)/2
if media >= 7:
    print("Aprovado")

else:
    print("Reprovado")
print("{} sua media é {}".format(nome,media))