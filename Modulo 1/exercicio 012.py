preço = float(input("Qual é o preço do produto ? R$"))
desconto = preço * 0.05
novo = preço - desconto
print("O produto que custava R${}, na promoção com desconto de 5% vai custar R${:.2f}".format(preço,novo))