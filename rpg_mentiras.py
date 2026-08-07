print('===  Criaçao de personagem do sistema REVENGE OF KRAT  ===')
print('primeiro pense em um conceito de personagem relacionado a Lies of P, ' \
'Pode ser desde um espreitador, nobre ou artesão. Feito isso de um nome para seu personagem')
nome = str(input('Qual o nome do seu personagem?: ')).strip()

print('Distribua os valores 1, 2 e 3 entre os atributos ' \
'Firmeza: atributo ligado ao corpo, força e resistência; ' \
'Sutileza: Atributo ligado a movimentos precisos, rápidos ou mesmo silenciosos; ' \
'Eloquência: Atributo ligado à interação social, performances e influência')
fir= int(input('Qual seu valor de Firmeza?: '))
sut= int(input('Qual o seu valor de Sutileza?: '))
elo= int(input('Qual o seu valor de Eloquência?: '))
foco_fir = foco_sut = foco_elo = False

print('Alguns valores que sao derivados dos atributos são a defesa que é 11 + sutileza + bonus e a integridade que é 14 + firmeza')
defesa = 11 + sut
integri = 14 + fir

print('')
print('Agora escolha o seu Camiho de combate entre:\n' 
'1-Caminho do Grilo - Equilíbrio. Escolha mais 1 aptidão especializada\n' 
'2-Caminho do Bastardo - Destreza.\n'
'3-Caminho do Varredor - Força. Receba Foco em Firmeza. e escolha entre um sub-caminho:\n'
)
cami = int(input('Coloque o numero do caminho que quer seguir: '))
if cami == 1:
    print('Caminho do grilo, equilibrado e esperto. Agora escolha o seu sub-caminho do grilo:\n' 
    '1-Beleza dos espinhos: Aumenta todos seus danos em 1 \n' \
    '2-Desabrochar precoce: Sempre começa a sessão com 3 cargas de fábula a mais\n')
    sub = int(input('coloque o numero do sub-caminho que quer seguir:'))
    cami_es = str('Grilo')
    if sub == 1:
        print('O escolhido foi o Beleza dos espinhos!')
        sub_es = str('Beleza dos espinhos: Aumenta todos seus danos em 1 ')
    else:
        print('O escolhido foi o Desabrochar precoce!')
        sub_es = str('Desabrochar precoce: Sempre começa a sessão com 3 cargas de fábula a mais')
if cami == 2:
    print('Caminho do Bastardo, nobre e elegante. Agora escolha o seu sub-caminho:\n' \
    '1-Abrir do Guarda-chuva: Recebe foco em Sutileza e +2 de Defesa\n' \
    '2-Espiral dançante: Recebe foco em Eloquência e soma seu valor a esquiva ao invés da Sutileza\n')
    sub = int(input('Coloque o numeor do sub-caminho que quer seguir:'))
    cami_es = str('Bastardo')
    if sub == 1:
        print('O escolhido foi o Abrir do Guarda-chuva!')
        sub_es = str('Abrir do Guarda-chuva: Recebe foco em Sutileza e +2 de Defesa')
        defesa = defesa + 2
        foco_sut = True
    else:
        print('O escolhido foi o Espiral dançante!')
        sub_es = str('Espiral dançante: Recebe foco em Eloquência e soma seu valor a esquiva ao invés da Sutileza')
        defesa = 11 + elo
        foco_elo = True
if cami == 3:
    print('Caminho do Varredor firme e resiliente. Agora escolha o seu sub-caminho:\n' \
    '1-Chifres de cabra: recebe 2 de redução a todo tipo de dano\n' \
    '2-Martelo Foguete: aumenta em 2 seus danos corpo a corpo\n')
    sub = int(input('Coloque o numero do sub-caminho:'))
    cami = str('Varredor')
    foco_fir = True
    if sub == 1:
        print('O escolhido foi Chifres de Cabra')
        sub_es = str('Chifres de cabra: recebe 2 de redução a todo tipo de dano')
    else:
        print('O escolhido foi Martelo Foguete')
        sub_es = str('Martelo Foguete: aumenta em 2 seus danos corpo a corpo')

esp = str(input('Qual as suas aptidões especializadas?: ')).strip()
secu =str(input('Qual as suas aptidões secundarias?: ')).strip()

print('\n===== FICHA DO PERSONAGEM =====')
print('Nome:{}'.format(nome.capitalize()))
print('Firmeza:{}({})| Sutileza:{}({})| Eloquencia:{}({})'
      .format(fir, 'X' if foco_fir else '',
              sut, 'X' if foco_sut else '',
              elo, 'X' if foco_elo else ''))
print('Defesa:{}'.format(defesa))
print('Integridade:{}'.format(integri))
print('Caminho de combate:{}|{}'.format(cami_es, sub_es))
print('Cargas de fabula:0/10')
print('Cargas braço legionario:10/10')
print('Apitiidoes Especializadas:{}'.format(esp))
print('Apitidoes Secundarias:{}'.format(secu))
print('=======================================')
