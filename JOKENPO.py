from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
comp = randint(0,2)

print('''Escolha uma das opções:
        [0] Pedra
        [1] Papel
        [2] Tesoura''')

jogador = int(input('Qual a sua jogada ? : '))
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO !!!")
sleep(1)

print('-='*13)
print(f'Computador jogou {itens[comp]}')
print(f'Jogador jogou {itens[jogador]}')
print('-='*13)

if comp == 0: # COMP JOGOU PEDRA
    if jogador == 0:
        print("EMPATE !")
    elif jogador == 1:
        print("JOGADOR VENCE !!!")
    elif jogador == 2:
        print("COMPUTADOR VENCE !!!")
    else:
        print('Jogada invalida !')

elif comp == 1: # COMP JOGOU PAPEL
    if jogador == 0:
        print("COMPUTADOR VENCE !!!")
    elif jogador == 1:
        print("EMPATE !!!")
    elif jogador == 2:
        print("JOGADOR VENCE !!!")
    else:
        print('JOGADA INVÁLIDA !')
elif comp == 2: # COMP JOGOU TESOURA
    if jogador == 0:
        print("JOGADOR VENCE !!!")
    elif jogador == 1:
        print("COMPUTADOR VENCE !!!")
    elif jogador == 2:
        print("EMPATE !!!")
    else:
        print('Jogada invalida !')


