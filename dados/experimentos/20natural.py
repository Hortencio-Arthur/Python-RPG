from random import randint
d = 0
cont = 0
while d != 20:
    d = randint(1, 20)
    print(d)
    cont += 1
print(f'Parabens! 20 natural... em {cont} tentativas')