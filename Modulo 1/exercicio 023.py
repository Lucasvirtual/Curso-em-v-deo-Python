numero = int(input("Informe um número: "))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print("Unidade: {}".format(u))
print("Unidade: {}".format(d))
print("Unidade: {}".format(c))
print("Unidade: {}".format(m))