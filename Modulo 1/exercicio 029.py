carro = int(input("Qual a velocidade que o carro passou ?"))
if carro >= 80:
    
    print("Você foi multado")
    limite = carro - 80
    multa = (7 * limite)
    print("Valor da multa R$",multa) 

else:
    print("Você não foi multado")
   