from random import randint
lado = int(input('Dado a ser rolado:d'))
bonus = int(input('Bonus da rolagem:'))
dado = randint(1, lado)

print(f'{dado}+{bonus}= {dado + bonus}')