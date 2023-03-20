import math
num1 = float(input("Comprimento do cateto oposto: "))
num2 = float(input("Comprimento do cateto adjacente: "))
hipo = math.hypot(num1, num2)
print ("A hipotenusa vai medir {:.2f}".format(hipo))