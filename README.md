# Python-RPG

Repositório pessoal onde reúno código em Python relacionado a RPG de mesa (TTRPG). É um espaço para praticar lógica de programação, modularização e reaproveitamento de código.

## Estrutura

### `ferramentas_rpg/` — biblioteca de ferramentas
Biblioteca feita para ajudar a evitar o retrabalho de código. Por enquanto conta apenas com o módulo dados.

#### `dados`- módulo de rolagens e dados
Conjunto de funções para os tipos de dados e rolagens usados em TTRPGs. O objetivo é me desafiar a aplicar a lógica dos dados de forma modular, evitando retrabalho. A maioria dos projetos vão usá-la como biblioteca.

**Rolagens implementadas**

- [x] Rolagem básica
- [x] Rolagem com bônus
- [x] Rolagem múltipla
- [x] Rolagem múltipla com bônus
- [x] Rolagem explosiva
- [x] Pool de dados com sucesso para cima
- [x] Roll and Keep
- [x] Dado Fudge simples
- [x] Dado Fudge múltiplo

**Planejadas**

- [ ] Dados diferentes
- [ ] Pool de dados com sucesso para baixo
- [ ] Dado para chance

Estado: **em desenvolvimento**, é o foco atual.

### `sistemas/`

Projetos que recriam a lógica e as mecânicas de sistemas de RPG em Python.

#### Sistemas desenvolvidos até o momento:
- FATE Acelerado (terminado, sem modularização, sem uso de ferramentas_rpg)
- City of Mist v1 (terminado, sem modularização, sem uso de ferramentas_rpg)
- City of Mist v2 (terminado, com modularização, sem uso de ferramentas_rpg)

### `projetos/`

Projetos diversos ligados a RPG, como um bot inspirado nos bots de Discord para RPG. Estado: **fase inicial**, ainda pouco explorada, já que o foco até agora foi a biblioteca de dados.

## Como Usar

- Versão do Python: desenvolvido com Python 3.14.2
- Dependências: nenhuma, uso apenas a biblioteca padrão
- importação dados: `from ferramentas_rpg import dados`

## Exemplo de Uso
```python
# importação
from ferramentas_rpg import dados
# uso da função dado bônus, que recebe valor_d, número de lados do dado que será sorteado, e bônus, 
# número do bônus que será somado ao valor sorteado
print(dados.dado_bonus(valor_d=20, bonus=2))
# resultado: (13,15)
# a função retorna uma tupla com o valor sorteado (13) e o resultado final (15), que é a soma do valor sorteado com o bônus (13 + 2 = 15)
```
- Um detalhe é que o exemplo acima representa o sistema de rolagem básica de D&D-5e. De d20 + modificador de atributo. 

## O que estou praticando

- Modularização
- Evitar retrabalho, reaproveitando funções entre projetos
- Lógica por trás de cada mecânica de dados
