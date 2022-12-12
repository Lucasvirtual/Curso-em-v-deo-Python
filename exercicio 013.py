salario = float(input("Qual é o salário do funcionário ? R$"))
aumento = salario * 0.15
total = salario + aumento
print("Um funcionáario que ganhava R${}, com 15%, passa a receber R${:.2f}".format(salario,total))