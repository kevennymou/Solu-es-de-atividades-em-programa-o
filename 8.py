nome = input()
salfixo = float(input())
qtdevendas = float(input())

bonus = qtdevendas * (15 / 100)

total = salfixo + bonus

print("TOTAL = R$ %0.2f" % total)
