import random
from PIL import Image
from art import *
import time

print('carregando...')
time.sleep(5)
print('carregando......')
time.sleep(5)


jogadas = ['pedra','tesoura','papel']

while True:

    while True:
        try:
            jogador = str(input("Escolha: pedra, tesoura ou papel? "))
            if jogador in jogadas:
                print('Recebi sua jogada')
                break
            else:
                print("Não entendi, insira 'pedra','tesoura' ou 'papel'")
        except Exception:
            print("d")

    #

    escolhas_possiveis_computador = ['pedra','tesoura', 'papel']
    computador = random.choice(escolhas_possiveis_computador)

    if jogador == computador:
        print(f'O computador escolheu {computador}, você escolheu '+f'{jogador}. Deu Empate !')
        tprint("empate ...")
    elif jogador == 'pedra':
        if computador == 'tesoura':
            print(f'O computador escolheu {computador}, você escolheu '+f'{jogador}. Vitória !')
            tprint("Venceu")
        else:
            print(f'O computador escolheu {computador}, você escolheu '+f'{jogador}. Você perdeu')
            tprint("Perdeu")
    elif jogador == "papel":
        if computador == "pedra":
            print(f'O computador escolheu {computador}, você escolheu '+f'{jogador}. Vitória')
            tprint("Venceu")
        else:
            print(f'O computador escolheu {computador}, você escolheu '+f'{jogador}. Você Perdeu')
            tprint("Perdeu")
    elif jogador == "tesoura":
        if computador == "papel":
            print(f'O computador escolheu {computador}, você escolheu '+f'{jogador}. Vitória')
            tprint("Venceu")
        else:
            print(f'O computador escolheu {computador}, você escolheu '+f'{jogador}. Você Perdeu')
            tprint("Perdeu")

    novamente = input("Você quer jogar novamente? (digite sim caso queira): ")
    if novamente != 'sim':
        print("Fechando. Obrigado por jogar")
        time.sleep(5)
        break
