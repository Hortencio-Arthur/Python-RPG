
#- rodar 2d6 e somar eles
#- somar rotulos de vantagem e subtrair rotulos de fraqueza
#- medir e mostrar nives de sucesso, inclunido animal
#- formatar o resultado final

from random import randint


print('~~ROLAGEM CITY OF MIST~~')
rotulos_poder = rotulos_fraqueza = 0

while True:
    try:
        rotulos_poder = int(input('Rotulos de Poder: '))
        if rotulos_poder == 999:
            break
        rotulos_fraqueza = int(input('Rotulos de Fraqueza: '))
    except ValueError:
        print('Digite um numero inteiro.')
        continue
    poder = rotulos_poder - rotulos_fraqueza

    tem_animal = ' '
    while tem_animal not in 'SN':
        tem_animal = input('Tem animal?[S/N]: ').strip().upper()[0]

    dado_um = randint(1,6)
    dado_dois = randint(1, 6)
    soma = dado_um + dado_dois
    soma += poder
    resultado = ' '
    if soma <= 6:
        resultado = 'Fracasso!'
    elif soma <= 9:
        resultado = 'Sucesso Fraco!'
    elif soma >= 12 and tem_animal == 'S':
        resultado = 'Animal!!!'
    elif soma >= 10:
        resultado = 'Sucesso Forte!'

    print(f'[{dado_um}] + [{dado_dois}] + {poder} = {soma}')
    print(f'{resultado}')
    print('==' * 20)