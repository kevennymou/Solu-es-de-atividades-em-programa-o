salario = float(input())

if salario <= 400:
    novo = salario + (salario * 15 / 100)
    reajuste = salario * 0.15
    print("Novo salario: {:.2f}".format(novo))
    print("Reajuste ganho: {:.2f}".format(reajuste))
    print("Em percentual: 15 %")
elif salario >= 400.01 and salario <= 800:
    novo = salario + (salario * 12 / 100)
    reajuste = salario * 0.12
    print("Novo salario: {:.2f}".format(novo))
    print("Reajuste ganho: {:.2f}".format(reajuste))
    print("Em percentual: 12 %")
elif salario >= 800.01 and salario <= 1200:
    novo = salario + (salario * 10 / 100)
    reajuste = salario * 0.10
    print("Novo salario: {:.2f}".format(novo))
    print("Reajuste ganho: {:.2f}".format(reajuste))
    print("Em percentual: 10 %")
elif salario >= 1200.01 and salario <= 2000:
    novo = salario + (salario * 7 / 100)
    reajuste = salario * 0.07
    print("Novo salario: {:.2f}".format(novo))
    print("Reajuste ganho: {:.2f}".format(reajuste))
    print("Em percentual: 7 %")
elif salario > 2000:
    novo = salario + (salario * 4 / 100)
    reajuste = salario * 0.04
    print("Novo salario: {:.2f}".format(novo))
    print("Reajuste ganho: {:.2f}".format(reajuste))
    print("Em percentual: 4 %")
