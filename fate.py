from random import randint
escala = {
    -4 : 'Horripilante',
    -3 : 'Catastrofico',
    -2 : 'Terrivel',
    -1 : 'Ruim',
    0 :  'Mediocre',
    1 :  'Regular',
    2 :  'Razoavel',
    3 :  'Bom',
    4 :  'Otimo',
    5 :  'Excepcional',
    6 :  'Fantastico',
    7 :  'Epico',
    8 :  'Lendario',
}
simbolos ={1: '+', -1: '-', 0: ' '}
N = '\033[1m'
V = '\033[32m'
R = '\033[31m'
F = '\033[0m'
while True:
    try:
        soma = 0
        bonus = int(input('Bonus: '))
        if bonus == 999:
            print(f'{N}Encerrando...{F}')
            break
        for c in range(1,5):
            dfate = randint(-1, 1 )
            print(f'[{simbolos[dfate]}]', end= ' ')
            print(f'{bonus:+}' if c == 4 else '', end= '')
            soma += dfate
        soma += bonus
        cor = V if soma > 0 else(R if soma < 0 else N )
        print(f"\nO resultado foi {cor}{escala.get(soma, 'Alem da escala!')}: {soma:+}{F}")
        print('=' * 20)
    except ValueError:
        print(f'{R}Valor invalido digite um numero inteiro.{F}')
        continue