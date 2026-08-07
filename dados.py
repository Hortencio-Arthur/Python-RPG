from random import randint
quant = int(input('Numero de dados a ser rolados: '))
rolar = str(input('dado a ser rolado: '))
bonus = int(input('Bonus da rolagem: '))

if rolar == 'd20':
    dado = randint(1,20)
    print(dado + bonus)

elif rolar == 'd12':
    dado = randint(1, 12)
    print(dado + bonus)

elif rolar == 'd10':
    dado = randint(1,10)
    print(dado + bonus)

elif rolar == 'd8':
    dado = randint (1, 8)
    print(dado + bonus)

elif rolar == 'd6':
    dado = randint(1,6)
    print(dado + bonus)

elif rolar == 'd4':
    dado = randint(1,4)
    print(dado + bonus)

