cem = dinheiro // 100
dinheiro = dinheiro - (cem * 100)
cinquenta = dinheiro // 50
dinheiro = dinheiro - (cinquenta * 50)
vinte = dinheiro // 20
dinheiro = dinheiro - (vinte * 20)
dez = dinheiro // 10
dinheiro = dinheiro - (dez * 10)
cinco = dinheiro // 5
dinheiro = dinheiro - (cinco * 5)
dois = dinheiro // 2
dinheiro = dinheiro - (dois * 2)

print(cem, "nota(s) de R$ 100,00")
print(cinquenta, "nota(s) de R$ 50,00")
print(vinte, "nota(s) de R$ 20,00")
print(dez, "nota(s) de R$ 10,00")
print(cinco, "nota(s) de R$ 5,00")
print(dois, "nota(s) de R$ 2,00")
print(dinheiro, "nota(s) de R$ 1,00")
