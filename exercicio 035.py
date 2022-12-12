n1 = float(input("Digite o primeiro número"))
n2 = float(input("Digite o segundo número"))
n3 = float(input("Digite o terceiro número"))

if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print("Pode formar um triângulo")
else:
    print("Não formará um triângulo")
