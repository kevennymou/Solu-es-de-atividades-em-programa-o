horainicial, horafinal = input().split()
horainicial = int(horainicial)
horafinal = int(horafinal)
dia = 24
if horainicial > horafinal:
    horasjogadas = ((horainicial - 24) * -1) + horafinal
    print("O JOGO DUROU {} HORA(S)".format(horasjogadas))
elif horainicial == horafinal:
    print("O JOGO DUROU 24 HORA(S)")
elif horainicial < horafinal:
    horasjogadas = horafinal - horainicial
    print("O JOGO DUROU {} HORA(S)".format(horasjogadas))
