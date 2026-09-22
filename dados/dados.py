#rolagem basica X
#rolagem com bonus X
#rolagem multipla X
#rolagem de dano X
#rolagem explosiva X
#pool de dados X
#roll and Keep X
#dado fate
from random import randint

def dado_puro(valord=20):
    dado = randint(1, valord)
    return dado

def dado_bonus(valord=20, bonus=0):
    dado = dado_puro(valord)
    res = dado + bonus
    return res

def dados_multiplos(valord=20, quant=1):
    dados = list()
    for d in range(quant):
        dados.append(dado_puro(valord))
    return dados

def rolagem_dano(valord=6, quant=1, bonus=0):
    dados = dados_multiplos(quant, valord)
    total = sum(dados) + bonus
    return dados, bonus, total

def dado_explosivo(valord=4, bonus=0):
    roll = dado_puro(valord)
    dado = roll
    total = dado
    dados_extra = list()

    while True:
        if dado == valord:
            extra = dado_puro(valord)
            dado = extra
            total += extra
            dados_extra.append(extra)

        else:
            break

    total += bonus

    return roll, dados_extra, bonus, total

def dado_pool(valord=6, quant=4, valor_alvo=3):
    dados = dados_multiplos(valord, quant)
    resultados = list()

    for d in dados:
        if d >= valor_alvo:
            resultados.append(d)

    sucessos = len(resultados)

    return dados, resultados, sucessos

def dado_keep_maior(valord=20, quant=2):
    dados = dados_multiplos(valord, quant)
    maior = max(dados)
    return dados, maior

def dado_keep_menor(valord=20, quant=2):
    dados = dados_multiplos(valord, quant)
    menor = min(dados)
    return dados, menor

#testes
# print(dado_puro(20))
# print(dado_bonus(20, 5))
# print(dados_multiplos(2,8))
# print(rolagem_dano(2,8,2))
# print(dado_explosivo(2,2))
# print(dado_pool(6, 4, 3))
# print(dado_keep_maior(20,3))
print(dado_keep_menor(10, 6))