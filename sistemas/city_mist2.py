# funçao que roda dois dados X
# funçao que verifica se tem animal X
# funçao que mostra o nivel de sucesso X
# pedir o valor de poder positivo e negativo, somar no valor dos dados X
# menu de movimentos do jogador, mostrar descriçao do movimento selecionado,e dar chance de escolher um novo movimento
# depois de rolar os dados mostrar opçoes que o jogador pode escolher do movimento de acordo com o valor da rolagem

from random import randint

def rolar_dados():
    """
    joga dois dados de 6 lados e soma eles
    :return:
        tuple: tupla contendo (soma, dado_1, dado_2)
    """
    dado_1 = randint(1,6)
    dado_2 = randint(1, 6)
    soma = dado_1 + dado_2
    return soma, dado_1, dado_2

def definir_poder():
    """
    define o poder total do jogador para o movimento
    :return:
    int: soma do poder positivo (rotulos de poder + condiçoes) com o poder negativo (rotulos fraquezas + condiçoes)
    """
    rotulos_poder = int(input('Poder (rotulos de poder + condições): '))
    rotulos_fraqueza = int(input('Poder Negativo (rotulos de fraqueza + condições): '))
    return rotulos_poder - rotulos_fraqueza

def tem_animal():
    """
    pergunta se o jogador tem animal para o movimento
    :return:
    bollean: se tem o Animal(True) ou nao(False)
    """
    res = ' '
    while res not in 'SN':
        res = input('Tem o ANIMAL!!! habilitado para o movimento?: ').strip().upper()[0]
    if res == 'S':
        tem = True
    else:
        tem = False
    return tem

def nivel_sucesso(soma, animal):
    """
    calcula o nivel do sucesso com base no valor final e se o personagem tem o Animal habilitado
    :param soma: soma final resultante dos dados com o poder
    :param animal: ve se tem(True) ou nao(False) o Animal
    :return:
    string: o nivel de sucesso da rolagem(fracasso, sucesso fraco, sucesso forte, animal)
    """
    resultado = ''
    if soma <= 6:
        resultado = str('Fracasso!')
    elif soma <= 9:
        resultado = str('Sucesso Fraco!')
    elif soma >= 10:
        resultado = str('Sucesso Forte!')

    if soma >= 12 and animal:
        resultado = 'ANIMAL!!!'

    return resultado

while True:
    soma_roll, dado1, dado2 = rolar_dados()
    poder_final = definir_poder()
    if poder_final >= 999:
        break
    animal_final = tem_animal()
    soma_final = soma_roll + poder_final
    print(f'Poder = {poder_final}')
    print(f'Dados: [{dado1}] + [{dado2}] = {soma_roll}')
    print(f'Total: {soma_roll} + {poder_final} = {soma_final}')
    print(f'Resulto: {nivel_sucesso(soma_final, animal_final)}')
    print('=' * 40)