from random import randint
quant = int(input('quantidade:'))
dado = int(input('d:'))
bonus = int(input('bonus: '))
soma = 0
roll= 0
for c in range(1, quant+1):
    roll = randint(1, dado)
    print(f'[{roll}]', end = ' ')
    soma += roll
soma += bonus
print(f'+ {bonus} = {soma}')