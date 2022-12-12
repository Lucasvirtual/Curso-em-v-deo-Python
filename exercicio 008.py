medida = float(input("Digite um número para medir em metros: "))
cm = medida * 100
mm = medida * 1000
dm = medida * 10
km = medida / 1000
print("A medida de {:.0f}m, corresponde a {:.0f}cm e {:.0f}mm".format(medida,cm,mm))
print("A medida de {:.0f}m, corresponde a {:.0f}km".format(medida,km))
print("A medida de {:.0f}m, corresponde a {:.0f}dm".format(medida,dm))